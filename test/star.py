import sys
import pygame
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
        self._star_create()

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



    def _update_screen(self):
        '''最新の画面の描画'''
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()


class Star:
    '''星の画像について'''
    def __init__(self):
        


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
