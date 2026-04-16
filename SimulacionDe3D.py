import cv2
import numpy as np
import math

# Crear lienzo
img = np.zeros((800, 800, 3), dtype=np.uint8)

x1, y1 = 200, 200
length = 200

angle = math.radians(30)
angle2 = math.radians(150)

x2 = int(x1 + length * math.cos(angle))
y2 = int(y1 - length * math.sin(angle))  # negativo porque pantalla

cv2.line(img, (x1,y1), (x2,y2), (255,255,255), 2)
cv2.line (img, (x1, y1+50), (x2,y2+50), (255,255,255),2)
cv2.line(img, ())

# Mostrar
cv2.imshow("Isometrico", img)
cv2.waitKey(0)
cv2.destroyAllWindows()