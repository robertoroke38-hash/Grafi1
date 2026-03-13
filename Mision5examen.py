import cv2
import numpy as np
import math
# crear lienzo negro
lienzo = np.zeros((500,500,3), dtype=np.uint8)

t = 0

while t <= 6.28:

    x = int(250 + 150 * math.sin(3*t))
    y = int(250 + 150 * math.sin(2*t))

    cv2.circle(lienzo, (x,y), 1, (255,255,255), -1)

    t += 0.01

cv2.imshow("Curva", lienzo)
cv2.waitKey(0)
cv2.destroyAllWindows()
