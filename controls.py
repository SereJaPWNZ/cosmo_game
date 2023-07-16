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

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:  #
                # Отработка долгого зажатия кнопки вправо
                gun.mright = False

            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  #
                # Отработка долгого зажатия кнопки влево
                gun.mleft = False


def update_screen(bg_color, screen, gun):
    '''Обновление экрана'''
    gun.update_gun()
    gun.output()
    pygame.display.flip()