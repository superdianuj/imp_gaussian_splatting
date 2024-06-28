import os
import argparse
import cv2
import numpy as np
from pathlib import Path
import os
from PIL import Image
import torch
import torchvision.transforms.functional as tf
from loss_utils import ssim
from lpipsPyTorch import lpips
import json
from tqdm import tqdm
from image_utils import psnr

parser=argparse.ArgumentParser()
parser.add_argument('--dir',type=str,required=True,help='directory of images to render upon')
parser.add_argument('--gt_dir',type=str,required=True, help='directory of ultimate ground truths')
args=parser.parse_args()
dirr=args.dir
gs_dir=dirr+'_gs'
if os.path.exists(gs_dir):
    os.system(f'rm -rf {gs_dir}')

os.system(f'mkdir {gs_dir}')
if os.path.exists('dataset'):
    os.system('rm -rf dataset')

os.system(f'ns-process-data images --data {dirr} --output-dir dataset --num-downscales 1 --sfm-tool hloc')

os.system(f'mkdir {gs_dir}/groundtruth_imgs')

gt_img_names=sorted(os.listdir('dataset/images'),key=lambda x:int(x.split('_')[-1].split('.')[0]))
gt_img_paths=[os.path.join('dataset/images',gt_name) for gt_name in gt_img_names]
gt_imgs=[cv2.imread(pth) for pth in gt_img_paths]  # destination
org_img_names=os.listdir(args.dir)
org_img_paths=[os.path.join(args.dir,img_name) for img_name in org_img_names]
org_imgs=[cv2.imread(pth) for pth in org_img_paths]  # source

# I am using assumption that org_imgs and pseduo_imgs has same indices in their filename in foramt _i

mapping_img_names={}
for i in range(len(gt_img_names)):
    img_gt=gt_imgs[i]
    errors=np.array([np.mean((img_gt-img_org)**2) for img_org in org_imgs])
    min_indx=np.argmin(errors)
    mapping_img_names[int(org_img_names[min_indx].split('_')[-1].split('.')[0])]=int(gt_img_names[i].split('_')[-1].split('.')[0])-1

# now I need to create new_pseudo_gt_img_names from pseudo_get_img_names

pseudo_gt_img_names=sorted(os.listdir(args.gt_dir),key=lambda x:int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))
new_pseudo_names=[]
for name in pseudo_gt_img_names:
    print(name)
    print("--------")
    indx=int(name.split('_')[-1].split('.')[0])
    new_indx=mapping_img_names[indx]
    new_name=name.split('_')[0]+'_'+str(new_indx)+'.'+name.split('_')[-1].split('.')[-1]
    new_pseudo_names.append(new_name)

new_pseudo_names=sorted(new_pseudo_names,key=lambda x:int(x.split('_')[-1].split('.')[0]))
pseudo_gt_img_paths=[os.path.join(args.gt_dir,gt_name) for gt_name in new_pseudo_names]

print(new_pseudo_names)

print(len(pseudo_gt_img_paths))
# sdjf



os.system("ns-train splatfacto --data dataset  --viewer.quit-on-train-completion True --pipeline.model.cull_alpha_thresh 0.005 --pipeline.model.continue_cull_post_densification False nerfstudio-data --train-split-fraction 1.1 --eval_mode 'all'")

output_pth=os.listdir('outputs/dataset/splatfacto')[0]
config_pth=os.path.join(os.path.join('outputs/dataset/splatfacto',output_pth),'config.yml')
os.system(f'ns-render interpolate   --load-config {config_pth}   --pose-source eval   --frame-rate 100   --interpolation-steps 1   --output-path buffer.mp4')

buff_dirr='buffer.mp4'

cap = cv2.VideoCapture(buff_dirr)
os.system(f'mkdir {gs_dir}/rendered_imgs')
# Check if camera opened successfully
if (cap.isOpened()== False):
  print("Error opening video stream or file")

count=0
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
    if args.dir==args.gt_dir:
        gt_im=cv2.imread(gt_img_paths[count])
        cv2.imwrite(f'{gs_dir}/groundtruth_imgs/img_{count}.png',gt_im)
    else:
        tmp_pth=pseudo_gt_img_paths[count]
        print("++++++++++++")
        print(tmp_pth)
        gt_im=cv2.imread(tmp_pth)
        cv2.imwrite(f'{gs_dir}/groundtruth_imgs/img_{count}.png',gt_im)
    
    if frame.shape[0]==gt_im.shape[0] and frame.shape[1]==gt_im.shape[1]:
        cv2.imwrite(f'{gs_dir}/rendered_imgs/img_{count}.png',frame)
    else:
        frame=cv2.resize(frame,(gt_im.shape[0],gt_im.shape[1]))
        cv2.imwrite(f'{gs_dir}/rendered_imgs/img_{count}.png',frame)

    count+=1
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else:
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()

os.system('rm -rf buffer.mp4')



def readImages(renders_dir, gt_dir):
    renders = []
    gts = []
    image_names = []
    for fname in os.listdir(renders_dir):
        render = Image.open(os.path.join(renders_dir,fname))
        gt = Image.open(os.path.join(gt_dir,fname))
        renders.append(tf.to_tensor(render).unsqueeze(0)[:, :3, :, :].cuda())
        gts.append(tf.to_tensor(gt).unsqueeze(0)[:, :3, :, :].cuda())
        image_names.append(fname)
    return renders, gts, image_names

def evaluate(base_dir):

    renders_dir=base_dir+'/rendered_imgs'
    gt_dir=base_dir+'/groundtruth_imgs'

    renders, gts, image_names = readImages(renders_dir, gt_dir)

    ssims = []
    psnrs = []
    lpipss = []

    for idx in tqdm(range(len(renders)), desc="Metric evaluation progress"):
        ssims.append(ssim(renders[idx], gts[idx]))
        psnrs.append(psnr(renders[idx], gts[idx]))
        lpipss.append(lpips(renders[idx], gts[idx], net_type='vgg'))
    print("```============================================='''")
    print("  SSIM : {:>12.7f}".format(torch.tensor(ssims).mean(), ".5"))
    print("  PSNR : {:>12.7f}".format(torch.tensor(psnrs).mean(), ".5"))
    print("  LPIPS: {:>12.7f}".format(torch.tensor(lpipss).mean(), ".5"))
    print("")
    print("```============================================='''\n")
    text_file = open(f'{base_dir}/metrics.txt', "w")
    text_file.write("  SSIM : {:>12.7f}".format(torch.tensor(ssims).mean(), ".5"))
    text_file.write("  PSNR : {:>12.7f}".format(torch.tensor(psnrs).mean(), ".5"))
    text_file.write("  LPIPS: {:>12.7f}".format(torch.tensor(lpipss).mean(), ".5"))
    text_file.close()

evaluate(gs_dir)

os.system(f'ns-render interpolate   --load-config {config_pth}   --pose-source eval   --frame-rate 30   --interpolation-steps 30   --output-path {gs_dir}/rendering.mp4')
os.system('rm -rf outputs')
