import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread("C:\\Users\\rover\\OneDrive\\Pictures\\GD.jpeg", 0)
# Obtener el tamaño de la imagen
x, y = img.shape
# Definir el factor de escala
scale_x, scale_y = 2,2
# Crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)
# Aplicar el escalado
for i in range(x):
    for j in range(y):
        for dx in range(scale_x):
            for dy in range(scale_y):
                
                   scaled_img[int(i*scale_x+dx), int(j*scale_y+dy)] = img[i, j]

# Mostrar la imagen original y la escalada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada (modo raw)', scaled_img)
cv.waitKey(0)
cv.destroyAllWindows()