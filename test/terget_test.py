import sys
import pygame
import pygame.font
from pygame.sprite import Sprite


class TergetTest:
    '''ゲームの全体的な管理を行うクラス'''
    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('ターゲットを撃て！')

        #各種インスタンスの作成
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.rectangle = Rectangle(self)
        self.stats = GameStats(self)
        self.play_button = Button(self, 'Play')


    def run_game(self):
        '''ゲームのメインループを開始する。'''
        while True:
            self._check_events()

            if self.stats.game_active == True:
                self.ship.update()
                self._update_bullets()
                self._update_rectangle()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_keydown_events(self, event):
        '''キーを押すイベントに対応する。'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._start_game()
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        '''キーを離すイベントに対応する。'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _check_play_button(self, mouse_pos):
        '''プレイヤーが「Play」ボタンをクリックしたら新規ゲームを開始する。'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and self.stats.game_active == False:
            self._start_game()


    def _start_game(self):
        #ゲームの統計情報をリセットする。
        self.stats.reset_stats()
        self.stats.game_active = True

        #残った弾を破棄する・
        self.bullets.empty()

        #宇宙船を中央に配置する。
        self.ship.center_ship()

        #マウスカーソルを非表示にする。
        pygame.mouse.set_visible(False)


    def _fire_bullet(self):
        '''新しい弾を生成し、Bulletsグループに追加する。'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    def _update_bullets(self):
        '''弾の位置を更新し、古い弾を廃棄する。'''
        #弾の位置を更新する。
        self.bullets.update()

        #見えなくなった弾を廃棄する。
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_rectangle(self):
        '''長方形の動作について'''


    def _update_screen(self):
        '''画面上の画像を更新し、新しい画面に切り替える。'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #ゲームが非アクティブ状態の時に「Play」ボタンを描画する。
        if self.stats.game_active == False:
            self.play_button.draw_button()

        pygame.display.flip()


#完了
class Ship:
    '''操作する艦隊に関するクラス'''
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        #宇宙船の画像を読み込み、サイズを取得する。
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #新しい宇宙船を画面下部の中央に配置する。
        self.rect.midbottom = self.screen_rect.midbottom

        #宇宙船の水平位置の浮動小数点数を格納する。
        self.x = float(self.rect.x)

        #移動フラグ
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''移動フラグによって宇宙船の位置を更新する。'''
        #宇宙船のxの値を更新する(rectではない)。
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left == True and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #self.xからrectオブジェクトの位置を更新する。
        self.rect.x = self.x

    def blitme(self):
        '''宇宙船を現在位置に描画する。'''
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        '''宇宙船を画面の中央に配置する。'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


class Rectangle:
    '''的となる長方形に関するクラス'''
    def __init__(self, game):
        self.settings = game.settings
        self.screen = game.screen


#完了
class Bullet(Sprite):
    '''宇宙船から発射される弾に関するクラス'''
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.color = self.settings.bullet_color

        #弾のrectを(0, 0)の位置に作成してから、正しい位置を設定する。
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #弾の位置を浮動小数点数で保存する。
        self.y = float(self.rect.y)

    def update(self):
        '''画面上の弾を移動する'''
        #弾の浮動小数点数での位置を更新する。
        self.y -= self.settings.bullet_speed
        #rectの位置を更新する
        self.rect.y = self.y

    def draw_bullet(self):
        '''画面に弾を描画する'''
        pygame.draw.rect(self.screen, self.color, self.rect)


#完了
class Settings:
    '''初期設定などに関するクラス'''
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #宇宙船の設定
        self.ship_speed = 1.5
        self.ship_limit = 3

        #弾の設定
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

#完了
class GameStats:
    '''ゲームの統計情報を管理するクラス'''
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        '''ゲーム中に変更される統計情報を初期化する。'''
        self.ships_left = self.settings.ship_limit


#完了
class Button:
    '''ボタンに関するクラス'''
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        #ボタンの大きさと属性を設定する。
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #ボタンのrectオブジェクトを生成し、画面の中央に配置する。
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #ボタンのメッセージは一度だけ準備する必要がある。
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        '''msgを画像に変換し、ボタンの中央に配置する。'''
        self.msg_image = self.font.render(msg, True, self.text_color,
                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        #空白のボタンを描画し、メッセージを描画する。
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


if __name__ == '__main__':
    #ゲームのインスタンスを作成し、ゲームを実行する。
    game = TergetTest()
    game.run_game()
