import pygame
import sys

'''上下左右に移動できるロケット'''

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption('ロケット操作')

        self.rocket = Rocket(self)

    def run_game(self):
        '''ゲームのメインループを開始する。'''
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()


    def _check_events(self):
        '''キーボードとマウスのイベントを監視する。'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        '''キーを押すイベントに対応する。'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        '''キーを離すイベントに対応する。'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        '''画面上の画像を更新し、新しい画面に切り替える。'''
        self.screen.fill(self.bg_color)
        self.rocket.blitme()

        pygame.display.flip()


class Rocket:
    def __init__(self, name):
        '''宇宙船を初期化し、開始時の位置を設定する。'''
        self.screen = name.screen
        self.screen_rect = name.screen.get_rect()

        #宇宙船の画像を読み込み、サイズを取得する。
        self.image = pygame.image.load('../alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        #ロケットを画面中央に配置する。
        self.rect.center = self.screen_rect.center

        #移動フラグ
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''移動フラグによって宇宙船の位置を更新する。'''
        #宇宙船のxの値を更新する(rectではない)。
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.x += 1
        if self.moving_left == True and self.rect.left > 0:
            self.rect.x -= 1
        if self.moving_up == True and self.rect.top > 0:
            self.rect.y -= 1
        if self.moving_down == True and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1

    def blitme(self):
        '''宇宙船を現在位置に描画する'''
        self.screen.blit(self.image, self.rect)

if __name__ == '__main__':
    #ゲームのインスタンスを作成し、ゲームを実行する。
    start = Game()
    start.run_game()
