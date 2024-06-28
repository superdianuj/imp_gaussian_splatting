import os
import cv2
import argparse
import torch
import numpy as np
import torchvision.transforms as transforms
from skimage.data import astronaut

parser=argparse.ArgumentParser()
parser.add_argument('--dir',required=True,type=str,help='directory of images')
parser.add_argument('--hor_blur',type=int,default=15,help='Y-axis blur parameters (horizonatal)')
parser.add_argument('--vert_blur',type=int,default=5,help='X-axis blur parameters (vertical)')
args=parser.parse_args()

dirr=args.dir
img_names=sorted(os.listdir(dirr),key=lambda x: int(x.split('_')[-1].split('.')[0]) if '_' in x else int(x.split('.')[0]))
img_dirs=[os.path.join(dirr,img_name) for img_name in img_names]

if os.path.exists(dirr+'_blurred'):
    os.system(f'rm -rf {dirr}_blurred')
os.system(f'mkdir {dirr}_blurred')

class MotionBlur(object):
    ''' Induces Motion Blurr on a given image (image must be padded to even dimensions)
        Inputs:
            a - horizontal motion factor
            b - vertical motion factor
        '''
    def __init__(self, a, b):
        self.a = abs(a)
        self.b = abs(b)

    def __call__(self, image):
        if (self.a == 0) and (self.b == 0):
            return image

        btch, c, n, m = image.shape

        # get values for a and b
        self.a = torch.distributions.Uniform(-self.a, self.a).sample((btch, 1))
        self.b = torch.distributions.Uniform(-self.b, self.b).sample((btch, 1))

        # compute FFT of image
        # image = image.double()
        F = torch.fft.fft2(image)

        # compute motion blurr function H in Frequency Domain
        u = torch.fft.fftfreq(n)[None, :].unsqueeze(0).repeat(btch, 1, 1)
        v = torch.fft.fftfreq(m)[:, None].unsqueeze(0).repeat(btch, 1, 1)

        omega = torch.pi*(u*self.a + v*self.b)
        H = (1/omega) * torch.sin(omega) * torch.exp(-(1.0j * omega))
        H[omega == 0] = 1

        H = H.reshape((btch, n, m))

        # perform motion blurring in Frequency Domain for each channel
        G = torch.zeros_like(F)
        for i in range(c):
            G[:, i, :, :] = F[:, i, :, :]*H

        # get blurred image
        return torch.abs(torch.fft.ifft2(G))

for i,img_dir in enumerate(img_dirs):
    img=cv2.imread(img_dir)
    image_tensor = transforms.ToTensor()(img)
    image_tensor=image_tensor.float()/255.0
    blurred_image_tensor = MotionBlur(args.vert_blur,args.hor_blur)(image_tensor.unsqueeze(0))
    blurred_image_tensor -= blurred_image_tensor.min()
    blurred_image_tensor /= blurred_image_tensor.max()
    blurred_img=blurred_image_tensor.permute(0,2,3,1).squeeze(0).numpy()
    blurred_img *=255
    blurred_img=blurred_img.astype(np.uint8)
    cv2.imwrite(f'{dirr}_blurred/img_{i}.png',blurred_img)
