
import numpy as np
import skimage.io as io
from matplotlib import pyplot as plt

img=io.imread("./astronaut.png")
#plt.imshow(img, cmap="gray",vmin=0,vmax=255)
#plt.show()

def add_gauss_noise(local_img,st_dev):
    gauss_matrix=np.random.normal(0,st_dev, img.shape)
    gauss_img=local_img+gauss_matrix
    gauss_img=np.clip(gauss_img,0,255)
    return gauss_img


def s_p_noise(local_img, pr):
    #s_p_array=np.random.choice([-255,0,255],img.shape,p=[probability/2,1-probability,probability/2])
    s_p_array=np.random.choice([-255,0,255],img.shape,p=[pr/2,1-pr,pr/2])
    s_p_img=local_img + s_p_array
    s_p_img= np.clip(s_p_img,0,255)
    return s_p_img

s_p=s_p_noise(img,0.1)
#plt.imshow(s_p, cmap="gray")
#plt.show()

g_p=add_gauss_noise(img,25)
plt.imshow(g_p, cmap="gray")
plt.show()


