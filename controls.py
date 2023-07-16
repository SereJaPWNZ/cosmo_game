import pygame, sys  # Обработка событий и закрытия окна

def events():
    '''Обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()