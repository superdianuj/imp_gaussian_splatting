import os
import cv2

dirr='results/SPSR/set5'
primary_dir=os.listdir(dirr)
primary_dir=[name for name in primary_dir if name.endswith('.png') or name.endswith('.jpg') or name.endswith('.JPG')]
file_names = sorted(primary_dir,key=lambda x: int(x.split('_')[-1].split('.')[0]))

# Full paths of the files
images_path = [os.path.join(dirr, file_name) for file_name in file_names if file_name.endswith('.JPG') or file_name.endswith('.png') or file_name.endswith('.jpg')]

if os.path.exists('superresolution_output'):
    os.system('rm -r superresolution_output')

os.mkdir('superresolution_output')

counter=0

for filename in images_path:
    img=cv2.imread(filename)
    cv2.imwrite('superresolution_output/processed_'+str(counter)+'.jpg',img)
    counter+=1

if os.path.exists('img_dataset'):
    os.system('rm -rf img_dataset')
