import numpy as np
from skimage import io
import matplotlib.pyplot as plt

# a) Lade das Bild 'astronaut.png' und spiegele es vertikal
img = io.imread('astronaut.png')
img_var1 = np.flipud(img)

# b) Spiegele das Originalbild horizontal
img_var2 = np.fliplr(img)

# c) Wende beide Spiegelungen nacheinander an
img_var3 = np.flipud(np.fliplr(img))

# d) Erzeuge ein neues Bild, das doppelt so hoch und breit ist wie das Bild 'astronaut.png'
#new_img = np.zeros((img.shape[0]*2, img.shape[1]*2, img.shape[2]))

x,y = shape= np.shape(img)
new_img= np.zeros((x*2,y*2))

# Fülle die vier Quadranten des neuen Bildes mit den verschiedenen Versionen des Originalbildes
new_img[y:y*2,0:x]= img
new_img[y:y*2,x:x*2]= img_var1
new_img[0:y,0:x]= img_var2
new_img[0:y,x:x*2]= img_var3




# new_img[:img.shape[0], :img.shape[1], :] = img
# new_img[:img.shape[0], img.shape[1]:, :] = img_var1
# new_img[img.shape[0]:, :img.shape[1], :] = img_var2
# new_img[img.shape[0]:, img.shape[1]:, :] = img_var3

# Zeige das neue Bild an
plt.imshow(new_img,cmap="gray",vmin=0,vmax=255)
plt.show()
