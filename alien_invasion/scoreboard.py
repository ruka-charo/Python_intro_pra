import pygame.font

class Scoreboard:
    '''得点の情報をレポートするクラス'''

    def __init__(self, ai_game):
        '''得点を記録するための属性を初期化する。'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #得点表示用のフォントを設定する。
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #初期の得点画像を準備する。
        self.prep_score()

    def prep_score(self):
        '''得点を描画用の画像に変換する。'''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        #画面の右上に得点を表示する。
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''画面に得点を描画する。'''
        self.screen.blit(self.score_image, self.score_rect)
