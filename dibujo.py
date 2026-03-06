import cv2 as cv
import numpy as np
img1 = cv.imread("C:\\Users\\rover\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-11-20 230752.png",1)
img1a = cv.cvtcolor(img1, cv.COLOR_BGR2GRAY)
x,y = img1.shape
img2= np.zeros((x,y), np.uint8)
for i in range (x):
    for j in range (y):
        img2[i,j]=255-img1a[i,a]

        '''
        if(img1[i,j]>150):
            img2[i,j]=255
        else:
            img2[i,j]=0
        '''

'''
x,y,z = img1.shape
print (x,y,z)
img2= np.zeros((x,y), np.uint8)
b,g,r= cv.split(img1)
mr = cv.merge([img2, img2, r])
mg = cv.merge([img2, g, img2])
mb = cv.merge([b, img2, img2])

nueva = cv.merge([r,g,b])
nueva2 = cv.merge([g,b,r])
nueva3 = cv.merge([b,r,g])

cv.imshow('n1', nueva)
cv.imshow('n2', nueva2)
cv.imshow('n3', nueva3)

cv.imshow('b', mb)
cv.imshow('g', mg)
cv.imshow('r', mr)
'''

cv.imshow('img1a', img1a)
cv.imshow('img1', img1)
cv.imshow('img', img1)
cv.waitKey(0)
cv.destroyAllWindows()

#OPERADOR PUNTUAL va checando pixel a pixel y los asigna dependiendo su valor a 0 o 255