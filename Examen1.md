#  Reporte de Misión: Graficación Táctica
**Agente Especial:** [Roberto Roque Cervantes:  24121345]

---
##  Evidencias de Misión


>Ejercicio 1
---

Imagen original
![Imagen original]("m1_oscura.jpg")

*Metodo raw*

```Python
img =cv2.imread("C:\\Users\\rover\\Downloads\\m1_oscura.png",0)
x, y = img.shape

#modo raw
for i in range(x):
    for j in range(y):
        img2= img[i][j]*50
        img[i][j] = np.clip(img2, 0, 255)
```
        
*Imagen generada*
![Imagen con ciclo (raw)]("por50.png")

*Metodo openCV*
-Desconozco si fue la forma correcta de usar la funcion pero me funciono

```Python
#modo cv
imgcv= cv2.multiply(img, 1)
```
con esa linea me dio el mismo resultado que con el uso de ciclos

Imagen generada
![Imagen OpenCV]("opencv50.png")


>Ejercicio 2
---

```Python
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\rover\\Downloads\\m2_mitad1.png")
img2= cv2.imread("C:\\Users\\rover\\Downloads\\m2_mitad2.png")

imagenN = np.zeros((400, 400, 3), dtype=np.uint8)
alto, ancho = img.shape[:2]

M1 = np.float32([
    [1,0,0],
    [0,1,0]
])

mitad1_t = cv2.warpAffine(img, M1, (400,400))

for i in range(200):
    for j in range(400):
        imagenN[i][j] = mitad1_t[i][j]



centro = (200,200)
rotacion=(180)
escala=1
M = cv2.getRotationMatrix2D(centro, rotacion, escala)
mitad_2 = cv2.warpAffine(img2, M, (400,400))
for i in range(200):
    for j in range(400):
        imagenN[i+200][j] = mitad_2[i+200][j]



cv2.imshow("Imagen Unida", imagenN)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Utilice los mismos ciclos que usaba en la tarea de misiones para la traslacion y rotacion y use ciclos for para recorrer las posiciones de la nueva imagen y colocar las imagenes fragmentadas, en la colocacion de la segunda imagen amplie 200 pixeles para colocarla debajo de la imagen 1

*Resultado*

![Imagen]("Union.png")

>Ejercicio 3
---
```Python
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

```

Resultado
![Imagen de dibujo]("m3_sello_forjado.png")

Utilice las primitivas de dibujo y al generar el lienzo, investigue el uso de ":" para rellenar toda la imagen generada con el color indicado en BGR

>Ejercicio 4

```Python
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
```

Imagen original:
![Imagen con ruido]("m4_ruido.png")

Aplico el uso de hsv con los limites de tonalidades y color, con el lower y upper, genero la mascara a mostrar y el resultado. Tambien utilizo el metodo blur en la mascara resultante para limpiar los ruidos sobrantes que siguen entrando en el color cian del texto.

*Imagen de color detectado*
![Imagen de color]("colorDetectado.png)

*Imagen de la mascara*
![Imagen de mascara]("mask.png")

>Ejercicio 5
---


```Python
import cv2
import numpy as np
import math
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

```
![Imagen de ecuacion]("curva.png")

Defino primero un ciclo while sea menro o igual a 2 pi, y aplique las ecuaciones, cambie los valores con la formacion de los puntos y hacer el incremento de 0.01

##  Análisis del Analista (Reflexiones Finales)

1. **Sobre los Operadores Puntuales (Misión 1):** Matemáticamente, ¿qué pasaría si en lugar de multiplicar por 50, hubieras sumado 50 a cada píxel oscuro? ¿Se revelaría el texto igual de claro o la imagen perdería contraste?
> *No seria lo mismo ya que elk contenido de intensidad de cada pixel tiene valores distintos, y la intensidad seria mucho menor que una multiplicacion, solamente cuidar que no exceda los limites de 255*

2. **Sobre el Espacio HSV (Misión 4):** ¿Por qué el modelo de color BGR es ineficiente para la Recuperación de Información cuando buscamos "todos los tonos de azul celeste", y por qué el modelo HSV resuelve este problema con una sola variable?
> *Por los valores que tiene cada tonalidad, depende mucho de los colores que se usen por ejemplo en bgr se requiere de 3 valores para una tonalidad, y no abarca todas las psoibles mientras que en hsv puedes establecer el rango abarcado de tonalidad*

3. **Sobre Ecuaciones Paramétricas (Misión 5):** ¿Por qué las ecuaciones paramétricas (usando el parámetro t) son mejores para dibujar formas cerradas y complejas en graficación por computadora que usar la clásica función $y=f(x)$?
> *Considero que sigue un patron mas preciso a la hora de generar cada punto en el patron, y tiene mas acertada la seccion y forma de graficar curvas complejas*

