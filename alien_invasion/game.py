import sys
from time import sleep
import  pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        pygame.display.set_caption('エイリアン侵略')

        #ゲームの統計情報を格納するインスタンスを生成する。
        self._make_instance()

        self._create_fleet()

        #難易度ボタンを作成する。
        self._make_button()


    def _make_instance(self):
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()


    def _make_button(self):
        self.easy_button = Button(self, 'easy')
        self.normal_button = Button(self, 'normal')
        self.difficult_button = Button(self, 'difficult')


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
                self._record_high_score()
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
            self._record_high_score()
            sys.exit()


    def _check_keyup_events(self, event):
        '''キーを離すイベントに対応する。'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _record_high_score(self):
        '''ハイスコアを記録する。'''
        if self.settings.easy_mode == True:
            self.settings.easy_mode = False
            with open('Easy_High_Score.txt', 'w') as f:
                f.write(str(self.stats.high_score))

        elif self.settings.normal_mode == True:
            self.settings.normal_mode = False
            with open('Normal_High_Score.txt', 'w') as f:
                f.write(str(self.stats.high_score))

        elif self.settings.difficult_mode == True:
            self.settings.difficult_mode = False
            with open('Difficult_High_Score.txt', 'w') as f:
                f.write(str(self.stats.high_score))


    def _check_play_button(self, mouse_pos):
        '''プレイヤーがボタンをクリックしたら新規ゲームを開始する。'''
        easy_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        normal_clicked = self.normal_button.rect.collidepoint(mouse_pos)
        difficult_clicked = self.difficult_button.rect.collidepoint(mouse_pos)


        if easy_clicked and self.stats.game_active == False:
            self._start_easy()
            self._first_action()

        elif normal_clicked and self.stats.game_active == False:
            self._start_normal()
            self._first_action()

        elif difficult_clicked and self.stats.game_active == False:
            self._start_difficult()
            self._first_action()


    def _start_easy(self):
        #ハイスコアを読み込む
        with open('Easy_High_Score.txt', 'r') as f:
            self.stats.high_score = int(f.readline())
        self.sb.prep_high_score()
        self.settings.easy_mode = True


    def _start_normal(self):
        #ハイスコアを読み込む
        with open('Normal_High_Score.txt', 'r') as f:
            self.stats.high_score = int(f.readline())
        self.sb.prep_high_score()
        self.settings.normal_mode = True
        self.settings.speedup_scale = 1.2


    def _start_difficult(self):
        #ハイスコアを読み込む
        with open('Difficult_High_Score.txt', 'r') as f:
            self.stats.high_score = int(f.readline())
        self.sb.prep_high_score()
        self.settings.difficult_mode = True
        self.settings.speedup_scale = 1.3


    def _first_action(self):
            self._start_game()
            self.settings.initialize_dynamic_settings()


    def _start_game(self):
        #ゲームの統計情報をリセットする。
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        #残ったエイリアンと弾を破棄する・
        self.aliens.empty()
        self.bullets.empty()

        #新しい艦隊を作成し、宇宙船を中央に配置する。
        self._create_fleet()
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

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        #弾とエイリアンの衝突に対応する。
        #その場合は対象の弾とエイリアンを廃棄する。
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, False, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            #艦隊を全滅させた時の処理
            self._start_new_level()


    def _start_new_level(self):
        #存在する弾を破壊し、新しい艦隊を作成する。
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        #レベルを増やす。
        self.stats.level += 1
        self.sb.prep_level()



    def _update_aliens(self):
        '''
        艦隊が画面の端にいるか確認してから、
        艦隊にいる前エイリアンの位置を更新する。
        '''
        self._check_fleet_edges()
        self.aliens.update()

        #エイリアンと宇宙船の衝突を探す。
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        #画面の一番下に到達したエイリアンを探す。
        self._check_aliens_bottom()


    def _ship_hit(self):
        '''エイリアンと宇宙船の衝突に対応する。'''
        if self.stats.ships_left > 0:
            #残りの宇宙船の数を減らし、スコアボードを更新する。
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            #残ったエイリアンと弾を破棄する。
            self.aliens.empty()
            self.bullets.empty()

            #新しい艦隊を生成し、宇宙船を中央に配置する。
            self._create_fleet()
            self.ship.center_ship()

            #一時停止する。
            sleep(0.5)

        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        '''エイリアンが画面の一番下に到達したかを確認する。'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #宇宙船を破壊した時と同じように扱う。
                self._ship_hit()
                break


    def _create_fleet(self):
        '''エイリアンの艦隊を作成する。'''
        #エイリアンを一匹作成し、一列のエイリアンの数を求める。
        #各エイリアンの間には、エイリアン一匹分のスペースを空ける。
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_alien_x = available_space_x // (2 * alien_width)

        #画面に収まるエイリアンの列数を決定する。
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (
        3 * alien_height + ship_height)
        number_rows = available_space_y // (2 * alien_height)

        #エイリアン艦隊を作成する。
        for row_number in range(number_rows):
            for alien_number in range(number_alien_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        #エイリアンを一匹作成し、列の中に配置する。
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.y = alien_height + (2 * alien_height * row_number)
        alien.rect.y = alien.y
        self.aliens.add(alien)


    def _check_fleet_edges(self):
        '''エイリアンが画面の端に達した場合、適切な処理を行う。'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        '''艦隊を下に移動し、横移動の方向を変更する。'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _update_screen(self):
        '''画面上の画像を更新し、新しい画面に切り替える。'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #得点の情報を描画する。
        self.sb.show_score()

        #ゲームが非アクティブ状態の時に「Play」ボタンを描画する。
        if self.stats.game_active == False:
            self.easy_button.draw_button()
            self.normal_button.draw_button()
            self.difficult_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    #ゲームのインスタンスを作成し、ゲームを実行する。
    ai = AlienInvasion()
    ai.run_game()
