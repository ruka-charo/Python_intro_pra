import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Hiragino Sans'

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4)
ax.plot(input_value, squares, linewidth=3)

#グラフのタイトルと軸のラベルを設定する。
ax.set_title('Sequare Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#メモリラベルのサイズを設定する。
ax.tick_params(axis='both', labelsize=14)

plt.show()
