class Settings:
    '''エイリアン侵略の全設定を格納するクラス'''

    def __init__(self):
        '''ゲームの初期設定'''
        #画面に関する設定
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #宇宙船の設定
        self.ship_speed = 2.0
        self.ship_limit = 3

        #弾の設定
        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #エイリアンの設定
        self.aliens_speed = 1.5
        self.aliens_close_speed = 10
        #1 → 下, -1 → 上
        self.aliens_direction = 1
