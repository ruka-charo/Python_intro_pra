from plotly.graph_objs import Bar, Layout
from plotly import offline
from die_class import Die


#D6を作成する。
die_1 = Die()
die_2 = Die()
die_3 = Die()

#サイコロを転がし、結果をリストに格納する。
results = []

for i in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)


#結果を分析する。
frequencies = []
max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_results+1):
    frequency = results.count(value)
    frequencies.append(frequency)


#結果を可視化する。
x_values = list(range(3, max_results+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '結果', 'dtick': 1}
y_axis_config = {'title': '発生した回数'}
my_layout = Layout(title='3個の6面サイコロを10000回転がした結果',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')
