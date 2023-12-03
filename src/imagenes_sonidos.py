import pygame


# IMAGENES 
#imagen 
imagen_personaje = pygame.image.load("./src/imagenes/donna.png")

imagen_malos = pygame.image.load("./src/imagenes/gatozombie.png")

coins_imagen = pygame.image.load("./src/imagenes/coins.png")

hueso_imagen=pygame.image.load("./src/imagenes/hueso1.png")

fondo = pygame.image.load("./src/imagenes/paisaje.png").convert()

inicio = pygame.image.load("./src/imagenes/inicio.jpg").convert()

pausa = pygame.image.load("./src/imagenes/pause.jpg").convert()

game_over = pygame.image.load("./src/imagenes/game.over.jpg").convert()




#SONIDOS
musica_colision = pygame.mixer.Sound("./src/SONIDOS/ladra.mp3")
musica_coins = pygame.mixer.Sound("./src/SONIDOS/sonidocoin.mp3")
pygame.mixer.music.load("./src/SONIDOS/musica.ambiente.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
playing_music=True
game_over_sonido=pygame.mixer.Sound("./src/SONIDOS/game.over.mp3")
sonido_colision_laser=pygame.mixer.Sound("./src/SONIDOS/colision.mp3")