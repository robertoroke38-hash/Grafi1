import cv2
import numpy as np

img=cv2.imread("C:\\Users\\rover\\OneDrive\\Escritorio\\Tareas Grafi\\m4_ruido.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([80,100,100]) 
upper = np.array([100, 255, 255]) 
mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=mask)
mask = cv2.medianBlur(mask, 5)
cv2.imshow("Mascara", mask)
cv2.imshow("Imagen Original", img)
cv2.imshow("Color Detectado", result)

cv2.waitKey(0)
cv2.destroyAllWindows()