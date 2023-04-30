import numpy as np
from skimage.io import imread,imsave
from matplotlib import pyplot as plt

##Aufgabe 1.1
img=imread("./astronaut.png")
plt.imshow(img, cmap="gray", vmin=0, vmax=255)

#print(type(img))
#print("My info: "+ str(img.dtype))

black=img[340:430,120:220]

imsave("./astroModified.png",black)

plt.imshow(black, cmap="gray", vmin=0, vmax=255)

#plt.show()

##Aufgabe 1.2
imagecopy1=img.copy() #Nur Fotokopien lassen sich bearbeiten
imagecopy1[10:50,105:130] =0

#Wenn eine Arrayreihe bzw. Pixel auf 0 gesetzt wird,
#erkennt man Unterschied nicht

#Helm wird geschwärzt
imagecopy2=img.copy()
imagecopy2[330:520,250:550]=0

plt.imshow(imagecopy2, cmap="gray", vmin=0, vmax=255)

#print(img.shape)

plt.show()


