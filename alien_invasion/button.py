import pygame.font


class Button:

    def __init__(self, ai_game, msg):
        '''ボタンの属性を初期化する。'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings

        #ボタンの大きさと属性を設定する。
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #ボタンのrectオブジェクトを生成し、画面に配置する。
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        if msg == 'easy':
            self.rect.midtop = self.screen_rect.midtop
        elif msg == 'normal':
            self.rect.center = self.screen_rect.center
        elif msg == 'difficult':
            self.rect.midbottom = self.screen_rect.midbottom

        #ボタンのメッセージは一度だけ準備する必要がある。
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        '''msgを画像に変換し、ボタンの中央に配置する。'''
        self.msg_image = self.font.render(msg, True, self.text_color,
                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()

        if msg == 'easy':
            self.msg_image_rect.midtop = self.rect.midtop
        elif msg == 'normal':
            self.msg_image_rect.center = self.rect.center
        elif msg == 'difficult':
            self.msg_image_rect.midbottom = self.rect.midbottom


    def draw_button(self):
        #空白のボタンを描画し、メッセージを描画する。
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
