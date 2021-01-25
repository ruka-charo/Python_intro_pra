from random import randint


class Die:
    '''１個のサイコロを表すクラス'''

    def __init__(self, num_sides=6):
        '''６面のサイコロをデフォルトにする。'''
        self.num_sides = num_sides


    def roll(self):
        '''１から麺の数の間のランダムな数値を返す。'''
        return randint(1, self.num_sides)
