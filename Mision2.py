import cv2
import numpy as np
import math
img =cv2.imread("C:\\Users\\rover\\Downloads\\qr_rotado.jpg")
alto, ancho = img.shape[:2]

rotada = np.zeros_like(img)


grados = math.radians(45)

cos_t = math.cos(grados)
sin_t = math.sin(grados)

cx = ancho // 2
cy = alto // 2

for y in range(alto):
    for x in range(ancho):

        x0 = x - cx
        y0 = y - cy

        # aplicar rotación
        xr = x0 * cos_t - y0 * sin_t
        yr = x0 * sin_t + y0 * cos_t

        
        xr = int(xr + cx)
        yr = int(yr + cy)

        if 0 <= xr < ancho and 0 <= yr < alto:
            rotada[yr, xr] = img[y, x]



#Metodo openCV
centro = (ancho//2, alto//2)
rotacion=(-45)
escala=1
M = cv2.getRotationMatrix2D(centro, rotacion, escala)
opencv = cv2.warpAffine(img, M, (ancho, alto))



cv2.imshow("Original", img)
cv2.imshow("Rotada", rotada)
cv2.imshow("Rotada con openCV", opencv)
cv2.waitKey(0)
cv2.destroyAllWindows()