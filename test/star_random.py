import sys
import pygame
from pygame.sprite import Sprite
import random

class Window():

    def __init__(self):
        pygame.init()
        #ウィンドウの設定
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('星')

        #星の作成
        self.stars = pygame.sprite.Group()
        self._stars_group_create()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


    def _check_events(self):
        '''キーボード操作の設定'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _star_create(self):
        #星のサンプルを作成
        sample = Star(self)
        sample.rect.x = 40 * random.randint(1, 30)
        sample.rect.y = 40 * random.randint(1, 20)

        self.stars.add(sample)


    def _stars_group_create(self):
        #星のグループを作成
        model = Star(self)

        for i in range(50):
            self._star_create()


    def _update_screen(self):
        '''最新の画面の描画'''
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()


class Star(Sprite):
    '''星の画像について'''
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()


class Settings:

    def __init__(self):
        '''ゲームの初期設定'''
        #画面に関する設定
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (29, 46, 89)


if __name__ == '__main__':
    '''直接開かれた時に行う'''
    star = Window()
    star.run_game()
