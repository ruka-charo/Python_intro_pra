import pygame
import sys


'''青い背景のPygameウインドウを作成'''
'''好きなキャラを画面中央に表示させる'''
class BlueSky:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))
        self.bg_color = (0, 0, 255)

        pygame.display.set_caption('青い背景')
        self.chara = Charo(self)

    def run_screen(self):
        while True:
            self._event()
            self._screen()

    def _event(self):
        #イベント監視
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _screen(self):
        #画面を背景色で塗りつぶす
        self.screen.fill(self.bg_color)
        self.chara.blitme()
        pygame.display.flip()


class Charo:
    def __init__(self, test):
        self.screen = test.screen
        self.screen_rect = test.screen.get_rect()

        #画像の読み込み
        self.image = pygame.image.load('images/charo.bmp')
        self.rect = self.image.get_rect()

        #中央に配置
        self.rect.center = self.screen_rect.center

    def blitme(self):
        '''キャラクターを表示'''
        self.screen.blit(self.image, self.rect)

#ファイルを直接呼び出した時のみ実行
if __name__ == '__main__':
    ans_1 = BlueSky()
    ans_1.run_screen()
