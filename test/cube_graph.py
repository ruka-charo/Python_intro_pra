import matplotlib.pyplot as plt


#データ
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

#データをプロットする
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#軸の設定
ax.set_title('Cube Graph', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube Value', fontsize=14)
ax.axis([0, max(x_values), 0, max(y_values)])
ax.tick_params(axis='both', which='major', labelsize=14)

#グラブの表示
plt.show()
