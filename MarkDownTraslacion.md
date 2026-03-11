>Ejercicio 1 de Traslacion 11/03/26

Imagen original:
![vehiculo](file:///C:/Users/rover/OneDrive/Escritorio/Tareas%20Grafi/vehiculo.jpg)

Metodo Raw de traslacion de imagen
```python
img =cv2.imread("C:\\Users\\rover\\Downloads\\vehiculo.jpg")
alto, ancho = img.shape[:2]
dx= 300
dy=200

#metodo raw
centrado = np.zeros((alto, ancho, 3), dtype=np.uint8)

for y in range(alto):
    for x in range(ancho):

        nuevo_x = x + dx
        nuevo_y = y + dy
        if nuevo_x < ancho and nuevo_y < alto:
            centrado[nuevo_y, nuevo_x] = img[y, x]
            
```
Imagen centrada en raw:
![Screenshot 2026-03-11 134305](file:///C:/Users/rover/OneDrive/Escritorio/Tareas%20Grafi/Screenshot%202026-03-11%20134305.png)

Metodo de OpenCV
```python
#metodo openCV
M = np.float32([
    [1, 0, dx],
    [0, 1, dy]
])


opencv = cv2.warpAffine(img, M, (ancho, alto))
```
Imagen centrada con OpenCV

![Screenshot 2026-03-11 135120](file:///C:/Users/rover/OneDrive/Escritorio/Tareas%20Grafi/Screenshot%202026-03-11%20135120.png)

*Preguntas*
¿Notaste alguna diferencia de tiempo al procesar la imagen píxel por píxel con ciclos for (Modo Raw) en comparación con la función cv2.warpAffine de OpenCV? ¿Por qué crees que tu código manual tarda mucho más en ejecutarse?

*Respuesta*
Al iniciar el codigo se abre primero la ventana de la traslacion con openCV, a ojo es poca la diferencia pero es notorio, considero que es más lento pro el procesamiento de operaciones que realiza con la repetición de los ciclos for.

