import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores



display_width = 768
display_height = 800

def run():

    pygame.init()  # Инициализация pygame
    screen = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)  # создание
    # отображаемой
    # области для нашей игры
    pygame.display.set_caption("Космические защитники")  # Вывод названия игры
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets )
        if stats.run_game == True:
            screen.fill(bg_color)
            controls.update_screen(bg_color, screen, stats, sc, gun, inos,
                bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)

run()