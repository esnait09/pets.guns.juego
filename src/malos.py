from configuraciones import *
from imagenes_sonidos import*

#caracteristicas 
SPEED=4

menos_longitud = 50
menos_altura = 50

UR = 9
DR = 3
DL = 1
UL = 7

# SPEED = 4
menos_longitud = 50

menos_altura = 50

cant_enemigos = 6

velocidad_normal_enemigos=4



velocidad_original_enemigos = SPEED

#---FUNCIONES

def mover_enemigos(malos, width, height, SPEED):
    #controlamos los rebotes de los lados del mapa.

    for malo in malos:
        # Rebote en bordes de la pantalla
        if malo["rect"].right >= width:
            if malo["dir"] == DR:
                malo["dir"] = DL
            elif malo["dir"] == UR:
                malo["dir"] = UL
        elif malo["rect"].left <= 1:
            if malo["dir"] == DL:
                malo["dir"] = DR
            elif malo["dir"] == UL:
                malo["dir"] = UR
        elif malo["rect"].bottom >= height:
            if malo["dir"] == DR:
                malo["dir"] = UR
            elif malo["dir"] == DL:
                malo["dir"] = UL
        elif malo["rect"].top <= 1:
            if malo["dir"] == UL:
                malo["dir"] = DL
            elif malo["dir"] == UR:
                malo["dir"] = DR

    for malo in malos:
        # Movimiento de los enemigos
        if malo["dir"] == DR:
            malo["rect"].top += SPEED
            malo["rect"].left += SPEED
        elif malo["dir"] == DL:
            malo["rect"].top += SPEED
            malo["rect"].left -= SPEED
        elif malo["dir"] == UL:
            malo["rect"].top -= SPEED
            malo["rect"].left -= SPEED
        elif malo["dir"] == UR:
            malo["rect"].left += SPEED
            malo["rect"].top -= SPEED

def crear_enemigo(imagen=None,left =  0, top = 0 , ancho = 100, alto = 100, color = (255,255,255), dir = dir, velocidad = 5):
    #creamos al enemigo con las caracterisitcas que nos pide para formar un cuadrado
    # con las caracteristicas redimencionamos la imagen    
    rec=pygame.Rect(left,top,ancho,alto)
    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
        
    return{"rect": rec, "color":color, "dir":dir, "velocidad" : velocidad, "imagen":imagen}

def cargar_enemigos(malos, cantidad,imagen = None):
    #cargamos a los enemigos. elegimos la cantidad que queremos 
      for i in range(cantidad):
            malos.append(crear_enemigo(imagen,left = randint(5, 650), top =randint(20, 20), ancho = 100, alto = 100, color = 0, dir = UR))

def dibujar_enemigos(pantalla,malos):
    #dibujamos a todos los enemigos 
    for malo in malos:
        if malo["imagen"]:
            pantalla.blit(malo["imagen"], malo["rect"])
        else:
            pygame.draw.rect(pantalla, malo["color"], malo["rect"])

def nueva_oleada(pantalla, fuente, width, height, oleada, malos, cant_enemigos, imagen_malos):
    try:
        # Intenta cargar la nueva oleada de enemigos
        oleada += 1
        mostrar_texto(pantalla, f"¡ Oleada {oleada} !", fuente, (width // 2, height // 2), white, black)
        pygame.display.flip()
        pygame.time.delay(2000)  # Pausa por 2000 milisegundos (2 segundos) para que el mensaje sea visible
        cant_enemigos += 1
        cargar_enemigos(malos, cant_enemigos, imagen_malos)
    except Exception as e:
        # Maneja cualquier excepción que pueda ocurrir durante la carga de enemigos
        print(f"Error al cargar la nueva oleada: {e}")


    return oleada

def eliminar_todos_los_malos(malos):
    #eliminamos a los malos 
    malos.clear()

def colision_malos_laser(malos):
    #creamos la colsion del laser y el malo.
                  for malo in malos:
                        if laser:           
                              colision = False             
                              for malo in malos:
                                    if detectar_colision(malo["rect"],laser["rect"]):
                                          malos.remove(malo)
                                          colision = True
                                          sonido_colision_laser.play()
                              if colision == True:
                                    laser=None