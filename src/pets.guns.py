from importaciones import *

pygame.init()

# CONFIGURACIONES PANTALLA 
pantalla = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Pet.Guns")

#CONTROLAR FPS 
clock = pygame.time.Clock()

while True:
      #pantalla inicio
      pantalla.fill(black) 
      pantalla.blit(inicio, origin)
      wait_user_click(pantalla,button_comenzar,button_salir,button_musica_on,button_musica_off)
      pygame.display.flip()
      #----
      contador = 0
      texto = fuente.render(f"PUNTOS: {contador}",True,white,black)
      rect_texto = texto.get_rect()
      rect_texto = (0,0) 
      #-----
      vidas = 3
      is_running = True
      texto_lives = fuente.render(f"Vidas: {vidas}", True,white,black)
      rect_texto_live = texto_lives.get_rect(topright = (width, 0))
      #-----
      malos=[]
      cargar_enemigos(malos, cant_enemigos,imagen_malos)
      oleada = 0
      SPEED=2
      #-----
      SPEED_DONNA=4

      #actualizar eventos 
      while is_running:
            clock.tick(FPS)
            tiempo_transcurrido += clock.get_time()

            for eventos in pygame.event.get():
                  if eventos.type == pygame.QUIT:
                        sys.exit()
                        #movimientos de personaje principal 
                  if eventos.type == pygame.KEYDOWN:
                        if eventos.key == pygame.K_LEFT:
                              move_left = True
                              move_right = False
                        if eventos.key == pygame.K_RIGHT:
                              move_right = True
                              move_left = False
                        if eventos.key == pygame.K_DOWN:
                              move_down = True
                              move_up = False
                        if eventos.key == pygame.K_UP:
                              move_up = True
                              move_down = False
                  
                        # disparo de laser 
                        if eventos.key == pygame.K_w:
                             if not laser:
                              size_laser = (5,10)
                              speed_laser = 6
                              laser_width , laser_heigh = size_laser
                              midtop = donna["rect"].midtop
                              laser = crear_bloque(None,midtop[0]-laser_width /2 ,midtop[1] - laser_heigh, laser_width, laser_heigh, red,velocidad_y == speed_laser)

                        if eventos.key ==pygame.K_t:
                              trick_reverse=True
                        #movimientos personaje principal 
                  if eventos.type == pygame.KEYUP:
                        if eventos.key == pygame.K_LEFT:
                              move_left = False
                        if eventos.key == pygame.K_RIGHT:
                              move_right = False
                        if eventos.key == pygame.K_DOWN:
                              move_down = False
                        if eventos.key == pygame.K_UP:
                              move_up = False
                        if eventos.key == pygame.K_x:
                        #pausar musica de fondo 
                              if playing_music:
                                    pygame.mixer_music.pause()
                              else:
                                    pygame.mixer_music.unpause()
                              playing_music=not playing_music
                        #pausa juego 
                        if eventos.key == pygame.K_p:
                              if playing_music:
                                    pygame.mixer_music.pause()
                              pantalla.blit(pausa, origin)
                              pygame.display.flip()
                              wait_user()
                              if playing_music:
                                    pygame.mixer_music.unpause()
                              #trucos 
                        if eventos.key == pygame.K_t:
                              trick_reverse=False
            
            #movemos al personaje principal 
            mover_donna(donna["rect"], move_right, move_left, move_up, move_down, width, height, SPEED_DONNA)

           #movemos a los malos 
            mover_enemigos(malos, width, height, SPEED)
            
                  #detectamos colsion de los laser con los gatos 
            
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

                  #detectamos colision de los puntos con personaje principal 
                  for coin in coins:
                        if detectar_colision(coin["rect"],donna["rect"]):
                              coins.remove(coin)
                              contador += 1
                              texto = fuente.render(f"PUNTOS: {contador}",True,white,black)
                              rect_texto = texto.get_rect()
                              rect_texto = (0,0)
                              musica_coins.play()
                      
                        if len(coins) == 0:
                             cargar_nuevos_coins(coins,25,coins_imagen)

                  for malo in malos:
                        if detectar_colision(malo["rect"], donna["rect"]):
                              malos.remove(malo)
                              if vidas > 1 :
                                    musica_colision.play()
                                    vidas -=  1 
                                    texto_lives = fuente.render(f"Vidas: {vidas}", True,white,black)
                                    rect_texto_live = texto_lives.get_rect(topright = (width, 0))
                              else:
                                    is_running = False
                  for h in huesos:
                        if detectar_colision(h["rect"], donna["rect"]):
                              huesos.remove(h)
                              eliminar_todos_los_malos(malos)     

                  if len(malos) == 0:
                        oleada=nueva_oleada(pantalla, fuente, width, height, oleada, malos, cant_enemigos, imagen_malos)
                        SPEED+=1

                  if tiempo_transcurrido - tiempo_ultimo_hueso >= 15000:
                        cargar_nuevos_huesos(huesos, 1, hueso_imagen)
                        huesos_creados += 2
                        tiempo_ultimo_hueso = tiempo_transcurrido

                  # Si hay huesos en pantalla, los dibujamos y actualizamos el tiempo
                  if huesos_creados > 0:
                        dibujar_huesos(pantalla, huesos)

                   
            #MOVEMOS EL LASER 
            laser = mover_y_eliminar_laser(laser)
            pantalla.blit(fondo, [0,0]) 

            #CREAMOS UN TRUCO
            if  trick_reverse:
                  if laser: 
                       laser["velocidad_y"] += 10

            #ZONA DE DIBUJO
            if laser:
                  pygame.draw.rect(pantalla,laser["color"],laser["rect"])

            if contador == 20 : 
                  SPEED_DONNA=6

            pantalla.blit(texto,rect_texto)
            pantalla.blit(texto_lives,rect_texto_live)
            dibujar_coins(pantalla, coins)
            dibujar_coins(pantalla, malos)
            dibujar_huesos(pantalla,huesos)
            pantalla.blit(donna["imagen"],donna["rect"])

            pygame.display.flip()

            #JSON 
            high_score_file = "maximo_puntaje.json "
            gestionar_json(contador,high_score_file)
            max_contador = obtener_max_puntuacion(high_score_file)

      #PANTALLA FINAL 
      pantalla.fill(black) 
      game_over_sonido.play()
      pantalla.blit(game_over, origin)
      mostrar_texto(pantalla,f"max puntos: {max_contador}",fuente,(width // 2, 20),white,black)
      pygame.display.flip()
      wait_user()

terminar()