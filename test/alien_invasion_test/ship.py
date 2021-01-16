import pygame

class Ship:
    '''宇宙船を管理するクラス'''

    def __init__(self, ai_game):
        '''宇宙船を初期化し、開始時の位置を設定する。'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #宇宙船の画像を読み込み、サイズを取得する。
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #新しい宇宙船を画面左側中央に配置する。
        self.rect.midleft = self.screen_rect.midleft

        #宇宙船の垂直位置の浮動小数点数を格納する。
        self.y = float(self.rect.y)

        #移動フラグ
        self.moving_top = False
        self.moving_bottom = False


    def _assign_ship_center(self):
        #画面左側中央に配置
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)


    def update(self):
        '''移動フラグによって宇宙船の位置を更新する。'''
        #宇宙船のyの値を更新する(rectではない)。
        if self.moving_bottom == True and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_top == True and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        #self.yからrectオブジェクトの位置を更新する。
        self.rect.y = self.y


    def blitme(self):
        '''宇宙船を現在位置に描画する。'''
        self.screen.blit(self.image, self.rect)
