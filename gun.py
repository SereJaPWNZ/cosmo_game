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
        self.mleft = False


    def output(self):

        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        '''Обновление позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:  #
            # Обновление позиции пушки для движения вправо
            self.rect.centerx += 1

        elif self.mleft and self.rect.left > 0:  #
            # Обновление позиции пушки для перемещения влево
            self.rect.centerx -= 1


