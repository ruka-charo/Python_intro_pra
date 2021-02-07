import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Hiragino Sans'
from die_class import Die


'''サイコロを２個転がした時のシミュレーションをmatplotlibで行う。'''

die_1 = Die()
die_2 = Die()


#出た目の結果を格納する箱。
results =[]

for i in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


#ヒストグラムの作成。
plt.title('2個のサイコロを転がした時のヒストグラム')
plt.xlabel('出た目の和')
plt.ylabel('回数')

plt.hist(results, bins=11)
plt.show()
