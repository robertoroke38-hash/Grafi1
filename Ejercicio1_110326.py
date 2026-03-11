import cv2
import numpy as np

img =cv2.imread("C:\\Users\\rover\\Downloads\\vehiculo.jpg")
alto, ancho = img.shape[:2]
dx= 300
dy=200

#metodo raw
centrado = np.zeros((alto, ancho, 3), dtype=np.uint8)

for y in range(alto):
    for x in range(ancho):

        nuevo_x = x + dx
        nuevo_y = y + dy
        if nuevo_x < ancho and nuevo_y < alto:
            centrado[nuevo_y, nuevo_x] = img[y, x]





#metodo openCV
M = np.float32([
    [1, 0, dx],
    [0, 1, dy]
])

opencv = cv2.warpAffine(img, M, (ancho, alto))

cv2.imshow("Original", img)
cv2.imshow("Traslacion RAW", centrado)
cv2.imshow("centrado opencv", opencv)

cv2.waitKey(0)
cv2.destroyAllWindows()