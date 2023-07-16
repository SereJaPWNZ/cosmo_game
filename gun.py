import pygame


class Gun():
    def __init__(self, screen):
        '''Inizializatzia puski'''


        self.screen = screen
        self.image = pygame.image.load("images/Gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False


    def output(self):

        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        '''Обновление позиции пушки'''
        if self.mright:
            self.rect.centerx += 1


