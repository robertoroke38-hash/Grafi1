#  Luz en windows 
**Alumno:** [Roberto Roque Cervantes:  24121345]


---
```Python
import sys
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math #librerias para codigo
rotation = 0.0
light_mode = 0  # 0=Básica, 1=Múltiple, 2=Direccional, 3=Spotlight, 4=Colores
```

* Funcion para dibujado del ojo en base a esferas
```Python
def draw_two_spheres():
    """Dibuja las esferas formando el ojo"""
    glPushMatrix()
    
    # Esclerótica (blanco)
    glColor3f(1.0, 1.0, 1.0) #colores RGB
    glPushMatrix()
    glTranslatef(0.56, 0, 0) #movimiento en el plano tridimensional
    glutSolidSphere(0.6, 40, 40)
    glPopMatrix()
    
    # Iris (azul grisáceo)
    glColor3f(0.84, 0.85, 0.92)
    glPushMatrix()
    glTranslatef(0.49, 0, 0)
    glutSolidSphere(0.55, 35, 35)
    glPopMatrix()
    
    # Parte rosada del iris
    glColor3f(0.85, 0.67, 0.65)
    glPushMatrix()
    glTranslatef(0.7, 0, 0)
    glutSolidSphere(0.54, 35, 35)
    glPopMatrix()

    # Pupila (negro)
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(0.3, 0, 0)
    glutSolidSphere(0.4, 30, 30)
    glPopMatrix()
    
    glPopMatrix()
```



```Python
def setup_lighting_basic():
    glEnable(GL_LIGHTING) #activa la iluminacion de openGL
    glEnable(GL_LIGHT0)  #activa la luz 0
    glDisable(GL_LIGHT1) #desactiva otras luces
    glDisable(GL_LIGHT2)
    
    light_position = [3.0, 2.0, 3.0, 1.0] #da valores a la posicion de la luz
    light_diffuse = [1.0, 1.0, 1.0, 1.0] #Modo de luz usado difuso
    light_ambient = [0.3, 0.3, 0.3, 1.0] #luz ambiental para iluminacion general
    
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
```