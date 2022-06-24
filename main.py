import cv2
import numpy as np
import imutils

image = cv2.imread('src/src.png')
alto, ancho, _ = image.shape

# Traslación
# M = np.float32([[1,0,10], [0,1,100]])
# imgOut = cv2.warpAffine(image, M, (ancho, alto+1500))

# Rotación
# M = cv2.getRotationMatrix2D((ancho//2, alto//2), 90, 0.5)
# imgOut = cv2.warpAffine(image, M, (alto, ancho))

# Escalado
# imgOut = cv2.resize(image,(361, 250), interpolation=cv2.INTER_CUBIC)

# Escalado relación/aspecto
# imgOut = imutils.resize(image, width=300)
# imgOut = imutils.resize(image, height=300)

# Recortar una imagen
print('image.shape=', image.shape)
imgOut = image[110:350, 100:300]

cv2.imshow('Imagen de entrada', image)
cv2.imshow('Imagen de salida', imgOut)
cv2.waitKey(0)
cv2.destroyAllWindows()