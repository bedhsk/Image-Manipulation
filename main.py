import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('src/src.png')
image = cvtColor(image, cv2.COLOR_BGR2RGB)

# Importar imagen en escala de grises
# image = cvtColor(image, cv2.COLOR_BGR2GRAY)

# Rotación de imagen
alto, ancho, _ = image.shape
M = cv2.getRotationMatrix2D((alto//2, ancho//2), 13, 0.5)
imgOut = cv2.warpAffine(image, M, (alto, ancho))

# Mostrar imágen
plt.imshow(imgOut)
plt.show()