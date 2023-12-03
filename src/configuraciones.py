import pygame,sys
from random import randint

# Inicializar Pygame
pygame.init()

SIZE = (700,648)

# CONFIGURACIONES PANTALLA 
pantalla = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pet.Guns")

# CONTROLAR FPS 
clock = pygame.time.Clock()

#DATOS PRINCIPALES 
origin = (0, 0)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

width = 700
height = 648
centro_pantalla = (width//2,height//2)

FPS = 60

button_width=200
button_height=50

#botones de pantalla de inicio 
button_comenzar=pygame.Rect(400,200,button_width,button_height)
button_musica_on=pygame.Rect(400,300,button_width,button_height)
button_musica_off=pygame.Rect(400,400,button_width,button_height)
button_salir=pygame.Rect(400,500,button_width,button_height)


#-------------------contadores------

#contador de max puntos 
contador = 0
max_contador = 0

#-------------------------------
# ESCRIBO FUENTE 
fuente = pygame.font.SysFont(None ,48)
texto = fuente.render(f"PUNTOS: {contador}",True,white,black)
rect_texto = texto.get_rect()
rect_texto = (0,0) 

# -------------------funciones-------

def escribir_fuente():
      # ESCRIBO FUENTE 
      fuente = pygame.font.SysFont(None ,48)
      texto = fuente.render(f"PUNTOS: {contador}",True,white,black)
      rect_texto = texto.get_rect()
      rect_texto = (0,0) 

def iniciar_juego():
    pygame.init()

def configurar_pantalla():
    pantalla = pygame.display.set_mode(SIZE) 
    pygame.display.set_caption("Pet.Guns")

def controlar_fps():
      #CONTROLAR FPS 
      clock = pygame.time.Clock()

def terminar():
    pygame.quit()
    exit() 

def mostrar_texto(superficie,texto,fuente,cordenadas,color_fuente,color_fondo=black):
     sup_texto=fuente.render(texto,True,color_fuente,color_fondo)
     rect_texto=sup_texto.get_rect()
     rect_texto.center =cordenadas
     superficie.blit(sup_texto,rect_texto)

def wait_user():
     while True:
          for e in pygame.event.get():
               if e.type == pygame.QUIT:
                    terminar()
               if e.type == pygame.KEYDOWN:
                  if e.key == pygame.K_ESCAPE:
                        terminar()
                  return

#crear cuadrado 
def crear_bloque(imagen = None, left=0,top=0,ancho=80,alto=100,color=(255,255,255),dir=0,borde=0,radio=1,velocidad_x=5,velocidad_y=5):
    rec=pygame.Rect(left,top,ancho,alto)
    if imagen:
        imagen = pygame.transform.scale(imagen, (ancho, alto))
    return{"rect": rec, "color":color, "dir":dir,"borde":borde, "radio":radio,"velocidad_x":velocidad_x,"velocidad_y":velocidad_y, "imagen" : imagen}


#para detectar colisiones 
def detectar_colision(rect_1,rect_2):
    colision=False
    if punto_en_rectangulo(rect_1.topleft,rect_2) or punto_en_rectangulo(rect_1.topright,rect_2)or punto_en_rectangulo(rect_1.bottomright,rect_2) or punto_en_rectangulo(rect_1.bottomleft,rect_2) or punto_en_rectangulo(rect_2.topleft,rect_1) or punto_en_rectangulo(rect_2.topright,rect_1)or punto_en_rectangulo(rect_2.bottomright,rect_1) or punto_en_rectangulo(rect_2.bottomleft,rect_1):
       colision=True
       return colision              

def punto_en_rectangulo(punto,rect):
    x,y=punto
    return x > rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom 



def crear_boton (screen, rect, texto, color_normal, color_hover):
    posicion_mouse = pygame.mouse.get_pos()

    if rect.collidepoint(posicion_mouse) :
        pygame.draw.rect(screen, color_hover, rect, border_radius = 0)
    else:
        pygame.draw.rect(screen, color_normal, rect, border_radius = 0)
    mostrar_texto_2(screen, texto, rect.centerx, rect.centery)


def mostrar_texto_2(superficie, texto, x, y, font_size = 36, color = (0, 0, 0)):
    fuente = pygame.font.SysFont("Minecraft", font_size)
    render = fuente.render(texto, True, color)
    rect_texto = render.get_rect(center = (x, y))
    superficie.blit(render, rect_texto)



def wait_user_click(screen, button_comenzar, button_salir, button_musica_on, button_musica_off):
    while True:
        crear_boton(screen, button_comenzar, "Comenzar", white, red)

        crear_boton(screen, button_musica_on, "Musica On", white, red)

        crear_boton(screen, button_musica_off, "Musica Off", white, red)

        crear_boton(screen, button_salir, "Salir", white, red)
        
        pygame.display.flip()

        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                terminar()

            if eventos.type == pygame.KEYDOWN:
                if eventos.key == pygame.K_ESCAPE:
                    terminar()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                if eventos.button == 1:
                    if button_comenzar.collidepoint(eventos.pos):
                        return None
                    elif button_salir.collidepoint(eventos.pos):
                        terminar()
                    elif button_musica_off.collidepoint(eventos.pos):
                        if pygame.mixer.music.get_busy():
                              pygame.mixer.music.pause()
                    elif button_musica_on.collidepoint(eventos.pos):
                        if not pygame.mixer.music.get_busy():
                              pygame.mixer.music.unpause()


