import cv2
import os
import imageio.v2 as imageio



def gifer(out_directory,gif_name,fps=10):
    if os.path.exists(gif_name):
        os.system(f'rm -rf {gif_name}')
    
    print("Current Directory:",out_directory)
    images=sorted(os.listdir(out_directory),key=lambda x:int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))

    # images.sort(key=lambda x:int(x.split('_')[-1].split['.'][0]) if '_' in x else int(x.split('.')[0]))
    images=[os.path.join(out_directory,img_name) for img_name in images]
    

    gif=[]
    for img in images:
        gif.append(imageio.imread(img))

    imageio.mimsave(gif_name,gif,fps=fps)
    print(f"--> Saved {gif_name}.")


if __name__=='__main__':
    curr_dir='.'
    dirr_list=os.listdir(curr_dir)
    if os.path.exists('GIF'):
        os.system('rm -rf GIF')
    os.system('mkdir GIF')
    for dirr in dirr_list:
        if not '.py' in dirr and not dirr=='GIF':
            gifer(dirr,'GIF/'+dirr+'.gif',fps=10)
     


