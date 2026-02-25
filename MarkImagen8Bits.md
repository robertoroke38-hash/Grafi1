>Dibujo de 8 bits usando cv2
```python
import cv2 as cv
import numpy as np
img=np.ones([360,300], np.uint8)*255
```
Con este segmento de codigo se genera el campo de pixeles que sera la imagen diseñada
```python
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
```

Utilice repeticion de ciclos for para la generacion de cada fila de tonalidad de grises dependiendo de los distintos colores que conformaban la imagen diseñada, cada "pixel" abarca un campo de 20x20 pixeles reales de la imagen, aqui un segmento del codigo, ya que todo el codigo forma la misma repeticion de ciclo saltando entre 20 y 20 pixeles.

![Imagen Generada](./Screenshot%202026-02-24%20201945.png)