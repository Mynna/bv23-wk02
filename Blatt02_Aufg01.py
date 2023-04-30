import numpy as np
from skimage.io import imread,imsave
from matplotlib import pyplot as plt

img=imread("./astronaut.png")
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

plt.show()



