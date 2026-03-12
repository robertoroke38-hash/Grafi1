import cv2
import numpy as np

img =cv2.imread("C:\\Users\\rover\\Downloads\\m1_oscura.png",0)
x, y = img.shape

#modo raw
for i in range(x):
    for j in range(y):
        img2= img[i][j]*50
        img[i][j] = np.clip(img2, 0, 255)



#modo cv
imgcv= cv2.multiply(img, 1)
#imgcv2= np.clip(imgcv,0,255)

cv2.imshow("Imagen por 50", img)
cv2.imshow("imagen cv", imgcv)
cv2.waitKey(0)
cv2.destroyAllWindows()