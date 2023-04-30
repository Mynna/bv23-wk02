import numpy as np
from skimage.io import imread,imsave
from matplotlib import pyplot as plt

img=imread("./astronaut.png")
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

#print(type(img))
#print("My info: "+ str(img.dtype))

black=img[340:430,120:220]

imsave("./astroModified.png",black)

plt.imshow(black, cmap="gray", vmin=0, vmax=255)


plt.show()



