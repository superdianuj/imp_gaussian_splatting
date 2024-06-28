import os
import cv2
import argparse



dirr='img_dataset'

new_dir='resized_shit'

if os.path.exists(new_dir):
    os.system(f'rm -rf {new_dir}')

os.system(f'mkdir {new_dir}')
        

dir_list=sorted(os.listdir(dirr),key=lambda x: int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))
im_paths=[os.path.join(dirr,curr_dir) for curr_dir in dir_list if curr_dir.endswith('png') or curr_dir.endswith('.jpg') or curr_dir.endswith('.JPG')]

counter=0
for pth in im_paths:
    img=cv2.imread(pth)
    new_pth=os.path.join(new_dir,'img_'+str(counter)+'.png')
    img_resized=cv2.resize(img,(550,550))
    cv2.imwrite(new_pth,img_resized)
    counter+=1

if os.path.exists('data'):
    os.system('rm -rf data')

os.system('mkdir data')
os.system('mkdir data/dataset')

