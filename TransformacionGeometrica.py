#La transformaicon geometrica es la traslacion de pixeles o imagenes
# operador de ventana es aquel que transforma un conjunto de pixeles
# negros de mierda
# Kernel de covolucion matriz de 3x3 o 5x5
#si se hace escalacion sin kernel hay perdida de datos


#primitivas de dibujo+
import cv2 as cv
import numpy as np 

img = np.ones((600,1000), np.uint8)*150 
cv.rectangle(img, (50,500), (650,250), (255,0,0), -1)
cv.line(img, (350,500), (350,100), (0), 4)
cv.line(img, (370,300), (400,300), (0), 4)
cv.line(img, (120,100), (560,100), (0), 4)
cv.line(img, (120,100), (50,250), (0), 4)
cv.line(img, (560,100), (650,250), (0), 4)
cv.line(img, (650,285), (850,340), (255, 0, 0), 70)
cv.line(img, (850,349), (850,470), (255, 0, 0), 70)
cv.line(img, (850,470), (600,470), (255, 0, 0), 70)
cv.rectangle(img, (600,500), (850,310), (255, 0, 0), -1)
cv.rectangle(img, (800,370), (850,310), (200, 200, 200), -1)
cv.line(img, (650,500), (650,250), (0), 4)
cv.line(img, (50,500), (50,250), (0), 4)
cv.circle(img, (180,500), 70, (0), -1 )
cv.circle(img, (700,500), 70, (0), -1 )
cv.circle(img, (180,500), 50, (120), -1 )
cv.circle(img, (700,500), 50, (120), -1 )

#for i in range(400):
    #cv.circle(img, (i,i), i , (255, 0, 0), -1 )
    #cv.rectangle(img, (10+i,10), (200,100), (34,56,100), -1)

    #cv.imshow('img', img)
    #img = np.ones((500,500,3), np.uint8)*150 
    #cv.waitKey(30)
    




cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()