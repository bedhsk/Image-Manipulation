from cv2 import cvtColor
import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('poligon.png')
image = cvtColor(image, cv2.COLOR_BGR2RGB)

# Importar imagen en escala de grises
# image = cvtColor(image, cv2.COLOR_BGR2GRAY)

# Rotación de imagen
alto, ancho, _ = image.shape
M = cv2.getRotationMatrix2D((alto//2, ancho//2), 0, 0.5)
imgOut = cv2.warpAffine(image, M, (alto, ancho))

#escala de imagen
def escala(x,y):
    imageOut = cv2.resize(image,(x,y), interpolation=cv2.INTER_CUBIC)
    plt.imshow(imageOut)
    plt.show()

#corta imagen
def cut_image(x1,y1,x2,y2):
    imageOut2= image[x1:y1,x2:y2]
    plt.imshow(imageOut2)
    plt.show()

# Mostrar imágen
#print(escala(100,200))
#print(cut_image(100,400,400,800))

# Mostrar imágen
#plt.imshow(imgOut)
#plt.show()