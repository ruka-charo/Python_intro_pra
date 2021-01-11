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


    def _star_create(self, num_x, num_y):
        #星のサンプルを作成
        sample = Star(self)
        sample_width, sample_height = sample.rect.size
        sample.rect.x = sample_width + (2 * sample_width) * num_x
        sample.rect.y = sample_height + (2 * sample_height) * num_y

        self.stars.add(sample)


    def _stars_group_create(self):
        #星のグループを作成
        model = Star(self)
        model_width, model_height = model.rect.size
        available_space_x = self.settings.screen_width - (2 * model_width)
        available_space_y = self.settings.screen_height - (2 * model_height)
        star_num_x = available_space_x // (2 * model_width)
        star_num_y = available_space_y // (2 * model_height)

        for num_x in range(star_num_x):
            for num_y in range(star_num_y):
                self._star_create(num_x, num_y)


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
        self.bg_color = (230, 230, 230)


if __name__ == '__main__':
    '''直接開かれた時に行う'''
    star = Window()
    star.run_game()
