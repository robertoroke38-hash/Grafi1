import cv2
import numpy as np

img = cv2.imread("C:\\Users\\rover\\Downloads\\frutas.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)#imagen en hsv

lower_green = np.array([35, 100, 100]) 
upper_green = np.array([85, 255, 255]) #entre menor rango menos objetos de valor se ven, si es mayor el rango hay mas objetos y se mezclan colores que no entran en el rango
lr = np.array([170,100,100])
ur = np.array([180,255, 255])
lb = np.array([20,110,110])
ub = np.array([35,255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)
mask2= cv2.inRange(hsv, lr, ur)
mask3= cv2.inRange(hsv, lb, ub)


result = cv2.bitwise_and(img, img, mask=mask)
result2 = cv2.bitwise_and(img, img, mask=mask2)
result3 = cv2.bitwise_and(img, img, mask=mask3)
cv2.imshow('mask', mask) #mascara
cv2.imshow("Imagen Original", img)
cv2.imshow("Color DetectadoG", result)
cv2.imshow("Color Detectado1", result2)
cv2.imshow("Color Detectado2", result3)
cv2.waitKey(0)
cv2.destroyAllWindows()