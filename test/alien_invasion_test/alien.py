import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #エイリアンの画像を読み込み、表示準備をする。
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.screen_width - self.rect.width
        self.rect.y = self.rect.height


    def update(self):
        '''エイリアンを動かす'''
        self.rect.y += (self.settings.aliens_speed *
                        self.settings.aliens_direction)


    def _alien_closer(self):
        '''エイリアンを動かす　その２'''
        self.rect.x -= self.settings.aliens_close_speed


    def blitme(self):
        #エイリアンを現在位置に表示させる。
        self.screen.blit(self.image, self.rect)
