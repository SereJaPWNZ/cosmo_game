import pygame, controls
from gun import Gun
from pygame.sprite import Group
from ino import Ino

def run():

    pygame.init()  # Инициализация pygame
    screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)  # создание
    # отображаемой
    # области для нашей игры
    pygame.display.set_caption("Космические защитники")  # Вывод названия игры
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    ino = Ino(screen)

    while True:
        controls.events(screen, gun, bullets )
        screen.fill(bg_color)
        controls.update_screen(bg_color, screen, gun, ino, bullets)
        controls.update_bullets(bullets)

run()