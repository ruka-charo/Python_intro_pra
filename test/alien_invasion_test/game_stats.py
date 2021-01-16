class GameStats:
    '''ゲームの統計情報を記録する。'''

    def __init__(self, ai_game):
        '''統計情報を初期化する。'''
        self.settings = ai_game.settings
        self.reset_stats()

        #ゲームをアクティブな状態で開始する。
        self.game_active = True

    def reset_stats(self):
        '''ゲーム内に更新される統計情報を初期化する。'''
        self.ship_left = self.settings.ship_limit
