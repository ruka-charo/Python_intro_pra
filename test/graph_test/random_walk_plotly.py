from plotly.graph_objs import Scatter,  Layout
from plotly import offline
from molecule_motion_class import RandomWalk


rw = RandomWalk(10000)
rw.fill_walk()


#グラフの作成
x_axis_config = {'title': 'x方向への移動'}
x_axis = rw.x_values
y_axis_config = {'title': 'y方向への移動'}
y_axis = rw.y_values

data = [Scatter(x=x_axis, y=y_axis)]

my_layout = Layout(title='ランダムウォーク',
                    xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='random_walk.html')
