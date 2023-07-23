import pygame


class Gun():
    def __init__(self, screen):
        '''Inizializatzia puski'''


        self.screen = screen
        self.image = pygame.image.load("images/Gun.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

        self.rect.centery = self.screen_rect.bottom - 64  # мои приколдесы
        # цифра равна половине размера картинки пушки
        self.center1 = float(self.rect.centery)  # мои приколдесы

        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

        self.mtop = False  # мои приколдесы
        self.mbottom = False  # мои приколдесы


    def output(self):

        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        '''Обновление позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:  #
            # Обновление позиции пушки для движения вправо
            self.center += 1.5

        elif self.mleft and self.rect.left > 0:  #
            # Обновление позиции пушки для перемещения влево
            self.center -= 1.5

        elif self.mbottom and self.rect.bottom < self.screen_rect.bottom:  #
            # Обновление позиции пушки для перемещения вниз
            self.center1 += 1.5

        elif self.mtop and self.rect.top > 0:  #
            # Обновление позиции пушки для перемещения вверх
            self.center1 -= 1.5


        self.rect.centerx = self.center
        self.rect.centery = self.center1


    def create_gun(self):
        '''размещает пушку в центре внизу после гибели'''
        self.center = self.screen_rect.centerx