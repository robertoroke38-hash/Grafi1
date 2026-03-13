import cv2
import numpy as np

img = cv2.imread("C:\\Users\\rover\\Downloads\\m2_mitad1.png")
img2= cv2.imread("C:\\Users\\rover\\Downloads\\m2_mitad2.png")

imagenN = np.zeros((400, 400, 3), dtype=np.uint8)
alto, ancho = img.shape[:2]

M1 = np.float32([
    [1,0,0],
    [0,1,0]
])

mitad1_t = cv2.warpAffine(img, M1, (400,400))

for i in range(200):
    for j in range(400):
        imagenN[i][j] = mitad1_t[i][j]



centro = (200,200)
rotacion=(180)
escala=1
M = cv2.getRotationMatrix2D(centro, rotacion, escala)
mitad_2 = cv2.warpAffine(img2, M, (400,400))
for i in range(200):
    for j in range(400):
        imagenN[i+200][j] = mitad_2[i+200][j]



cv2.imshow("Imagen Unida", imagenN)
cv2.waitKey(0)
cv2.destroyAllWindows()