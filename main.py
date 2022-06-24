import cv2
import numpy as np

image = cv2.imread('src/src.png')
alto, ancho, _ = image.shape

# Traslación
# M = np.float32([[1,0,10], [0,1,100]])
# imgOut = cv2.warpAffine(image, M, (ancho, alto+1500))

# Rotación
M = cv2.getRotationMatrix2D((ancho//2, alto//2), 180, -0.5)
imgOut = cv2.warpAffine(image, M, (alto, ancho))

cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imgOut)
cv2.waitKey(0)
cv2.destroyAllWindows()