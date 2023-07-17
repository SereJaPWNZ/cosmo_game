import pygame, sys  # Обработка событий и закрытия окна

def events(gun):
    '''Обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:  #
                # Отработка одиночного зажатия кнопки вправо
                gun.mright = True

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  #
                # Отработка одиночного зажатия кнопки влево
                gun.mleft = True

            if event.key == pygame.K_w or event.key == pygame.K_UP:  #
                # Отработка одиночного зажатия кнопки вправо
                gun.mtop = True

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:  #
                # Отработка одиночного зажатия кнопки влево
                gun.mbottom = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:  #
                # Отработка долгого зажатия кнопки вправо
                gun.mright = False

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  #
                # Отработка долгого зажатия кнопки влево
                gun.mleft = False

            elif event.key == pygame.K_w or event.key == pygame.K_UP:  #
                # Отработка долгого зажатия кнопки вверх
                gun.mtop = False

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:  #
                # Отработка долгого зажатия кнопки вниз
                gun.mbottom = False

def update_screen(bg_color, screen, gun):
    '''Обновление экрана'''
    gun.update_gun()
    gun.output()
    pygame.display.flip()