from configuraciones import *
from imagenes_sonidos import *


#creamos lista de moneda 
def cargar_nuevos_coins(coins, cantidad, imagen = None):
    #cargamos nuevos coins con la lista, cantidad y imagen. 

    for i in range(cantidad):
        coins.append(crear_bloque(imagen, randint(0,width-block_width),randint(50,height-size_coins), size_coins,size_coins))

def dibujar_coins(pantalla, coins):
    #dibujamos los coin y redimencionamos la imagen 
    for coin in coins:
        if coin["imagen"]:
            pantalla.blit(coin["imagen"], coin["rect"])
        else:
            pygame.draw.rect(pantalla, coin["color"], coin["rect"], coin["borde"], coin["radio"])

#especificaciones de la moneda 
block_width = 50
block_height = 50
velocidad_x = 5
velocidad_y = 5
size_coins = 30
color = red

coins = []
cargar_nuevos_coins(coins, 25, coins_imagen)

#-------------------------huesos-------------------------------------------

def cargar_nuevos_huesos(huesos, cantidad, imagen = None):
    #cargamos la cantidad de huesos que queremos. 
    for i in range(cantidad):
        huesos.append(crear_bloque(imagen, randint(0,width-block_width),randint(50,height-size_coins), 40,40))

def dibujar_huesos(pantalla, huesos):
    #dibujamos los huesos 
    for h in huesos:
        if h["imagen"]:
            pantalla.blit(h["imagen"], h["rect"])
        else:
            pygame.draw.rect(pantalla, h["color"], h["rect"], h["borde"], h["radio"])

huesos=[]
cargar_nuevos_huesos(huesos,1,hueso_imagen)

huesos_creados = 0
tiempo_huesos_en_pantalla = 0
tiempo_transcurrido = 0
tiempo_ultimo_hueso = 0