import pygame
import sys  # Обработка событий и закрытия окна


def run():

    pygame.init()  # Инициализация pygame
    screen = pygame.display.set_mode((1200, 700))  # создание отображаемой области для нашей игры
    pygame.display.set_caption("Космические защитники")  # Вывод названия игры
    bg_color = (0, 0, 0)

    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit()

        screen.fill(bg_color)
        pygame.display.flip()

run()