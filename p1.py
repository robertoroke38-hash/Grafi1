import cv2 as cv
import numpy as np
img=np.ones([360,300], np.uint8)*255

img[1,1]=0

for i in range(20, 40):
    for j in range(80, 180):
        img[i,j]=80

for i in range(40, 60):
    for j in range(60, 240):
        img[i,j]=80

for i in range(60, 80):
    for j in range(60, 125):
        img[i,j]=30

for i in range(60, 80):
    for j in range(125, 160):
        img[i,j]=140

for i in range(60, 80):
    for j in range(160, 180):
        img[i,j]=30

for i in range(60, 80):
    for j in range(180, 200):
        img[i,j]=140

for i in range(80, 100):
    for j in range(40, 60):
        img[i,j]=30

for i in range(80, 100):
    for j in range(60, 80):
        img[i,j]=140

for i in range(80, 100):
    for j in range(80, 100):
        img[i,j]=30

for i in range(80, 100):
    for j in range(100, 160):
        img[i,j]=140

for i in range(80, 100):
    for j in range(160, 180):
        img[i,j]=30

for i in range(80, 100):
    for j in range(180, 240):
        img[i,j]=140

for i in range(100, 120):
    for j in range(40, 60):
        img[i,j]=30

for i in range(100, 120):
    for j in range(60, 80):
        img[i,j]=140

for i in range(100, 120):
    for j in range(80, 120):
        img[i,j]=30

for i in range(100, 120):
    for j in range(120, 180):
        img[i,j]=140

for i in range(100, 120):
    for j in range(180, 200):
        img[i,j]=30

for i in range(100, 120):
    for j in range(200, 260):
        img[i,j]=140

for i in range(120, 140):
    for j in range(40, 80):
        img[i,j]=30

for i in range(120, 140):
    for j in range(80, 160):
        img[i,j]=140

for i in range(120, 140):
    for j in range(160, 240):
        img[i,j]=30

for i in range(140, 160):
    for j in range(80, 220):
        img[i,j]=140

for i in range(160, 180):
    for j in range(60, 180):
        img[i,j]=30

for i in range(160, 180):
    for j in range(100, 120):
        img[i,j]=80

for i in range(180, 200):
    for j in range(40, 240):
        img[i,j]=30

for i in range(180, 200):
    for j in range(100, 120):
        img[i,j]=80

for i in range(180, 200):
    for j in range(160, 180):
        img[i,j]=80

for i in range(200, 220):
    for j in range(20, 260):
        img[i,j]=30

for i in range(200, 220):
    for j in range(100, 180):
        img[i,j]=80

for i in range(220, 240):
    for j in range(20, 60):
        img[i,j]=140

for i in range(220, 240):
    for j in range(60, 80):
        img[i,j]=30

for i in range(220, 240):
    for j in range(80, 100):
        img[i,j]=80

for i in range(220, 240):
    for j in range(100, 120):
        img[i,j]=140

for i in range(220, 240):
    for j in range(120, 160):
        img[i,j]=80

for i in range(220, 240):
    for j in range(160, 180):
        img[i,j]=140

for i in range(220, 240):
    for j in range(180, 200):
        img[i,j]=80

for i in range(220, 240):
    for j in range(200, 220):
        img[i,j]=30

for i in range(220, 240):
    for j in range(220, 260):
        img[i,j]=140

for i in range(240, 260):
    for j in range(20, 80):
        img[i,j]=140

for i in range(240, 260):
    for j in range(80, 200):
        img[i,j]=80

for i in range(240, 260):
    for j in range(200, 260):
        img[i,j]=140

for i in range(260, 280):
    for j in range(20, 60):
        img[i,j]=140

for i in range(260, 280):
    for j in range(60, 220):
        img[i,j]=80

for i in range(260, 280):
    for j in range(220, 260):
        img[i,j]=140

for i in range(280, 300):
    for j in range(60, 120):
        img[i,j]=80

for i in range(280, 300):
    for j in range(160, 220):
        img[i,j]=80

for i in range(300, 320):
    for j in range(40, 100):
        img[i,j]=30

for i in range(300, 320):
    for j in range(180, 240):
        img[i,j]=30

for i in range(320, 340):
    for j in range(20, 100):
        img[i,j]=30

for i in range(320, 340):
    for j in range(180, 260):
        img[i,j]=30
        
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()