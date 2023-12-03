from configuraciones import *
from imagenes_sonidos import *


#velocidades y cordenadas 
cord_x = 400
cord_y = 300
speed_x = 0 
speed_y = 0

SPEED_DONNA=4

move_up = False
move_down = False
move_right = False
move_left = False

def mover_donna(donna_rect, move_right, move_left, move_up, move_down, width, height, SPEED_DONNA):
    # movemos al personaje principal y le damos limites  
                        # Rebote derecha pantalla
                        if move_right and donna_rect.right <= (width - SPEED_DONNA):
                              # Derecha
                              donna_rect.left += SPEED_DONNA
                        if move_left and donna_rect.left >= (0 + SPEED_DONNA):
                              # Izquierda
                              donna_rect.left -= SPEED_DONNA
                        if move_up and donna_rect.top >= SPEED_DONNA:
                              # Arriba
                              donna_rect.top -= SPEED_DONNA
                        if move_down and donna_rect.bottom < height - SPEED_DONNA:
                              # Abajo
                              donna_rect.top += SPEED_DONNA

def mover_y_eliminar_laser(laser):
    #creamos el laser en tipo cuadrado y lo movemos por el eje y. controlamos la desaparicion del laser 
    if laser:
        if laser["rect"].bottom >= 0:
            laser["rect"].move_ip(0, -laser["velocidad_y"])
        else:
            laser = None
    return laser


#bloque del personaje 
donna = crear_bloque(imagen_personaje,cord_x,cord_y,50,50,speed_x,speed_y)

#--------laser----------------------------------------------------------------
#LASER 
size_laser=(5,10)
speed_laser=6
laser = None

#TRUCOS
trick_reverse = False
