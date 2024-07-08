import os
import cv2
import numpy as np
import argparse

def calculate_psnr(img1, img2, max_value=255):
    mse = np.mean((np.array(img1, dtype=np.float32) - np.array(img2, dtype=np.float32)) ** 2)
    if mse == 0:
        return 100
    return 20 * np.log10(max_value / (np.sqrt(mse)+1e-8))



def main(gt_dir,target_dir):
    gt_img_names=os.listdir(gt_dir)
    gt_img_names=[img for img in gt_img_names if img.endswith('.png') or img.endswith('.jpg') or img.endswith('.JPG')]
    gt_img_pths=[os.path.join(gt_dir,img) for img in gt_img_names]

    target_img_names=os.listdir(target_dir)
    target_img_names=[img for img in target_img_names if img.endswith('.png') or img.endswith('.jpg') or img.endswith('.JPG')]
    target_img_pths=[os.path.join(target_dir,img) for img in target_img_names]
    
    real_psnr=[]
    with open("results.txt", "w") as text_file:
        for pth in gt_img_pths:
            img_gt=cv2.imread(pth)
            virtual_psnr=[]
            for pth_2 in target_img_pths:
                img_t=cv2.imread(pth_2)
                psnr=calculate_psnr(img_gt,img_t,max_value=255)
                virtual_psnr.append(psnr)
                
            psnr_r_ind=np.argmax(virtual_psnr)
            psnr_r=virtual_psnr[psnr_r_ind]
            target_img_pth_r=target_img_pths[psnr_r_ind]
            print(f"GT: {pth} | Target {target_img_pth_r}| PSNR: {psnr_r} dB", file=text_file)
            real_psnr.append(psnr_r)
            
            
    avg_psnr=np.mean(real_psnr)
    print(f"Average PSNR: {avg_psnr} dB")
            

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--gt_dir',type=str,required=True,help='ground truth directory')
    parser.add_argument('--target_dir',type=str,required=True,help='target directory')
    args=parser.parse_args()
    main(args.gt_dir,args.target_dir)
