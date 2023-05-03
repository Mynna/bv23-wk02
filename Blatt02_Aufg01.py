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

#plt.show()

##Aufgabe 1.3

# a) Lade das Bild 'astronaut.png' und spiegele es vertikal
#img = io.imread('astronaut.png')
img =imread('astronaut.png')

img_var1 = np.flipud(img)

# b) Spiegele das Originalbild horizontal
img_var2 = np.fliplr(img)

# c) Wende beide Spiegelungen nacheinander an
img_var3 = np.flipud(np.fliplr(img))

# d) Erzeuge ein neues Bild, das doppelt so hoch und breit ist wie das Bild 'astronaut.png'

x,y = shape= np.shape(img)
new_img= np.zeros((x*2,y*2))

# Fülle die vier Quadranten des neuen Bildes mit den verschiedenen Versionen des Originalbildes
new_img[y:y*2,0:x]= img
new_img[y:y*2,x:x*2]= img_var2
new_img[0:y,0:x]= img_var1
new_img[0:y,x:x*2]= img_var3

# Zeige das neue Bild an
plt.imshow(new_img,cmap="gray",vmin=0,vmax=255)
#plt.show()

##Aufg. 1.4
brosche= img[340:430,120:220]
#brosche[0,0]=0 #"ein Pixel" auf schwarz; funktioniert nur bei ipynb, aber nicht py
plt.imshow(img,cmap="gray",vmin=0,vmax=255)
#plt.show()

#Antwort: es findet eine Änderung im Originalbild statt

##Aufg. 1.5
mask=np.zeros(img.shape)
mask[340:430,120:220]=1
maskedImg= img*mask
plt.imshow(maskedImg,cmap="gray",vmin=0,vmax=255)
plt.show()



