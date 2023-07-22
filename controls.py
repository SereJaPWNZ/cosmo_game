import pygame, sys # Обработка событий и закрытия окна
from bullet import Bullet
from ino import Ino

def events(screen, gun, bullets):
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

            elif event.key == pygame.K_w or event.key == pygame.K_UP:  #
                # Отработка одиночного зажатия кнопки вправо
                gun.mtop = True

            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:  #
                # Отработка одиночного зажатия кнопки влево
                gun.mbottom = True

            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

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

def update_screen(bg_color, screen, gun, inos, bullets):
    '''Обновление экрана'''
    gun.update_gun()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    '''Обновление позиции пуль'''
    bullets.update()
    for bullet in bullets.copy():
         if bullet.rect.bottom <= 0:
              bullets.remove(bullet)
    # print(len(bullets))  # Проверка на очистку пуль при выходе за экран


def update_inos(inos):
    '''обновляет позицию пришельцев'''
    inos.update()


def create_army(screen , inos):
    '''создание армии пришельцев'''
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((800 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 128 - 2 * ino_height) / ino_height)


    for row_number in range(number_ino_y):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)