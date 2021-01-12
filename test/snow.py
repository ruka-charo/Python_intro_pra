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
        pygame.display.set_caption('雪の降る丘')

        #雪の作成
        self.snows = pygame.sprite.Group()
        self._snows_group_create()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self._update_snow()


    def _check_events(self):
        '''キーボード操作の設定'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _snow_create(self, num_x):
        #雪のサンプルを作成
        sample = Snow(self)
        sample_width, sample_height = sample.rect.size
        sample.rect.x = sample_width + (2 * sample_width) * num_x

        self.snows.add(sample)


    def _snows_group_create(self):
        #雪のグループを作成
        model = Snow(self)
        model_width, model_height = model.rect.size
        available_space_x = self.settings.screen_width - (2 * model_width)
        available_space_y = self.settings.screen_height - (2 * model_height)
        snow_num_x = available_space_x // (2 * model_width)
        snow_num_y = available_space_y // (2 * model_height)

        for num_x in range(snow_num_x):
            self._snow_create(num_x)


    def _update_snow(self):
        for snow in self.snows.sprites():
            snow.y = float(snow.rect.y)
            snow.y += self.settings.snow_speed
            snow.rect.y = snow.y


    def _update_screen(self):
        '''最新の画面の描画'''
        self.screen.fill(self.settings.bg_color)
        self.snows.draw(self.screen)
        pygame.display.flip()


class Snow(Sprite):
    '''雪の画像について'''
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load('images/snow_fragment.bmp')
        self.rect = self.image.get_rect()


class Settings:

    def __init__(self):
        '''ゲームの初期設定'''
        #画面に関する設定
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        #雪の降る速度
        self.snow_speed = 2.0


if __name__ == '__main__':
    '''直接開かれた時に行う'''
    snow = Window()
    snow.run_game()
