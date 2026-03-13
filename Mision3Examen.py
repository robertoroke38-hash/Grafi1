import cv2
import numpy as np

imagenCLAVE = np.zeros((500, 500, 3), dtype=np.uint8)
imagenCLAVE[:] = (50,20,20)

cv2.circle(imagenCLAVE, (250,250), 100, (0,255,255), 3 )
cv2.rectangle(imagenCLAVE, (200,200), (300,300), (0, 0, 255), -1)
cv2.line(imagenCLAVE, (0,0), (500,500), (255,255,255), 2)
cv2.line(imagenCLAVE, (0,500), (500,0), (255,255,255), 2)


cv2.imshow("m3_sello_forjado.png", imagenCLAVE)
cv2.waitKey(0)
cv2.destroyAllWindows()
