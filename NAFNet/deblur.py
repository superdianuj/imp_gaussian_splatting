import os
import cv2



dirr='img_dataset'

if os.path.exists('resized'):
    os.system('rm -rf resized')
os.system('mkdir resized')

if os.path.exists('deblur_output'):
    os.system('rm -rf deblur_output')

os.system('mkdir deblur_output')

img_names=sorted(os.listdir(dirr),key=lambda x: int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))
img_paths=[os.path.join(dirr,img_name) for img_name in img_names if img_name.endswith('.png') or img_name.endswith('.jpg') or img_name.endswith('.JPG')]

count=0
for img_path in img_paths:
    img=cv2.imread(img_path)
    img_resized=cv2.resize(img,(256,256))
    cv2.imwrite(f'resized/img_{count}.png',img_resized)
    count+=1

paths=sorted(os.listdir(dirr),key=lambda x: int(x.split('.')[0]))

for pth in paths:
    curr_path=os.path.join('resized',pth)
    os.system(f'python basicsr/demo.py -opt options/test/GoPro/NAFNet-width64.yml --input_path {curr_path} --output_path deblur_output/{pth}')


os.system(f'rm -rf {dirr}')