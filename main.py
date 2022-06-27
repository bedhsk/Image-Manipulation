from cv2 import cvtColor
import numpy as np
import cv2
import matplotlib.pyplot as plt
import tkinter

image = cv2.imread('src/src.png')
image = cvtColor(image, cv2.COLOR_BGR2RGB)

# Importar imagen en escala de grises
# image = cvtColor(image, cv2.COLOR_BGR2GRAY)

# Rotación de imagen
alto, ancho, _ = image.shape
M = cv2.getRotationMatrix2D((alto//2, ancho//2), 13, 0.5)
imgOut = cv2.warpAffine(image, M, (alto, ancho))

#escala de imagen
def escala(x,y):
    imageOut = cv2.resize(image,(x,y), interpolation=cv2.INTER_CUBIC)
    plt.imshow(imageOut)

#corta imagen
def cut_image(x1,y1,x2,y2):
    imageOut2= image[x1:y1,x2:y2]
    plt.imshow(imageOut2)

# Mostrar imágen
plt.imshow(imgOut)
plt.show()