import os
import cv2
import numpy as np


img_dir1='strategy_1_results'
img_dir2='strategy_2_results'

if os.path.exists('combined_imgs'):
    os.system('rm -r combined_imgs')
    
os.system('mkdir combined_imgs')


img_dir1_imgs=sorted(os.listdir(img_dir1),key=lambda x:int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))
img_dir2_imgs=sorted(os.listdir(img_dir2), key=lambda x: int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split['.'][0]))
img_dir1_imgs=[os.path.join(img_dir1,img) for img in img_dir1_imgs]
img_dir2_imgs=[os.path.join(img_dir2,img) for img in img_dir2_imgs]


assert len(img_dir1_imgs)==len(img_dir2_imgs)
alpha=0.8
for i in range(len(img_dir1_imgs)):
    img_1=cv2.imread(img_dir1_imgs[i])
    img_2=cv2.imread(img_dir2_imgs[i])
    im_mask=255 * np.ones(img_2.shape, img_2.dtype)
    print(im_mask.shape,im_mask.dtype)
    center = (img_1.shape[1]//2, img_2.shape[0]//2)
    print(center)
    combined_img = cv2.seamlessClone(img_2, img_1, im_mask, center, cv2.MIXED_CLONE)
    cv2.imwrite(f'combined_imgs/{i}.png',combined_img)

