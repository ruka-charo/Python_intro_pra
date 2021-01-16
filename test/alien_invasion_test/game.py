import sys
import  pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class AlienInvasion:
    '''ゲームのアセットと動作を管理する全体的なクラス'''

    def __init__(self):
        '''ゲームを初期化し、ゲームのリソースを作成する。'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
        #フルスクリーンにしたい場合は…。
        #self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption('エイリアン侵略(縦ver.)')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_aliens()

        self.stats = GameStats(self)

        print('宇宙船の残機：', self.stats.ship_left)


    def run_game(self):
        '''ゲームのメインループを開始する。'''
        while True:
            self._check_events()

            if self.stats.game_active == True:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
        if event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        '''キーを離すイベントに対応する。'''
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False


    def _create_aliens(self):
        '''エイリアン艦隊の作成'''
        #作成範囲の計算
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        available_x = self.settings.screen_width - (
        6 * self.ship.rect.width + 2 * alien_width)
        available_y = self.settings.screen_height - (
        2 * alien_height)

        alien_num_x = available_x // (2 * alien_width)
        alien_num_y = available_y // (2 * alien_height)

        #艦隊の作成
        for i in range(alien_num_x):
            for k in range(alien_num_y):
                self._assign_aliens(i, k)


    def _assign_aliens(self, i, k):
        '''エイリアン艦隊の作成の続き'''
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.rect.x = (self.settings.screen_width - alien_width
        - (2 * alien_width) * i)
        alien.rect.y = alien_height * (2 * k + 1)

        self.aliens.add(alien)


    def _change_direction(self):
        '''エイリアンの移動　その1'''
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self.settings.aliens_direction = -1
                self._aliens_closer()

            elif alien.rect.top <= 0:
                self.settings.aliens_direction = 1
                self._aliens_closer()


    def _aliens_closer(self):
        '''エイリアンの移動　その2'''
        for alien in self.aliens.sprites():
            alien._alien_closer()


    def _aliens_advance(self):
        '''エイリアンが左端に到達した時の挙動'''
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self.aliens_ship_collision()
                break


    def aliens_ship_collision(self):
        if self.stats.ship_left >= 1:
            #機体残数を減らし、画面にあるものを一旦全て削除する。
            self.stats.ship_left -= 1
            print('宇宙船の残機：', self.stats.ship_left)
            self.aliens.empty()
            self.bullets.empty()
            #船とエイリアンを再構築する。
            self._create_aliens()
            self.ship._assign_ship_center()
            #衝突時に一時停止
            sleep(0.5)

        else:
            self.stats.game_active = False


    def _update_aliens(self):
        '''エイリアン関係の更新'''

        self.aliens.update()
        self._change_direction()
        self._aliens_advance()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.aliens_ship_collision()


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
            if bullet.rect.left >= self.ship.screen_rect.right:
                self.bullets.remove(bullet)

        self._check_aliens_bullets_collision()


    def _check_aliens_bullets_collision(self):
        #弾がエイリアンに当たったかを調べる
        #その場合は対象の弾とエイリアンを廃棄する。
        collisions = pygame.sprite.groupcollide(
                    self.bullets, self.aliens, True, True)

        if not self.aliens:
            #存在する弾を破壊し、新しい艦隊を作成する。
            self.bullets.empty()
            self._create_aliens()


    def _update_screen(self):
        '''画面上の画像を更新し、新しい画面に切り替える。'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    #ゲームのインスタンスを作成し、ゲームを実行する。
    ai = AlienInvasion()
    ai.run_game()
