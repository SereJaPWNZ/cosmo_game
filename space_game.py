import pygame, controls
from gun import Gun

def run():

    pygame.init()  # Инициализация pygame
    screen = pygame.display.set_mode((700, 800))  # создание отображаемой области для нашей игры
    pygame.display.set_caption("Космические защитники")  # Вывод названия игры
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:

        controls.events()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()

run()