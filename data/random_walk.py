from random import choice


class RandomWalk:
    '''ランダムウォークを生成するためのクラス'''

    def __init__(self, num_points=5000):
        '''ランダムウォークの属性を初期化する。'''
        self.num_points = num_points

        #全てのランダムウォークは(0,0)から開始する。
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        '''ランダムウォークの全ての点を計算する。'''

        #全てのステップ数が指定した数になるまでランダムウォークを続ける。
        while len(self.x_values) < self.num_points:

            #移動する方向と距離を決定する。
            x_step = self._get_step()
            y_step = self._get_step()

            #どこにも移動しない場合は結果を破棄する。
            if x_step == 0 and y_step == 0:
                continue

            #新しい位置を計算する。
            self._new_step(self.x_values, self.y_values,
                            x_step, y_step)


    def _get_step(self):
        #移動する方向と距離を決定する。
        direction = choice([-1, 1])
        distance = choice(range(5))

        return distance * direction


    def _new_step(self, x_values, y_values, x_step, y_step):
        #新しい位置を計算する。
        x = x_values[-1] + x_step
        y = y_values[-1] + y_step

        x_values.append(x)
        y_values.append(y)
