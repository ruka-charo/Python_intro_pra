import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = '/Users/rukaoide/Library/Mobile Documents/\
com~apple~CloudDocs/Documents/Python/Python_intro_pra/\
data/data_sample/San_Francisco.csv'


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, row in enumerate(header_row):
        if row == 'DATE':
            index_date = index
        elif row == 'TMAX':
            index_tmax = index
        elif row == 'TMIN':
            index_tmin = index

    #ファイルから日付、最高気温、最低気温を抜き出す。
    days, max_t, min_t = [], [], []

    for row in reader:
        day = datetime.strptime(row[index_date], '%Y-%m-%d')
        max = int(row[index_tmax])
        min = int(row[index_tmin])
        days.append(day)
        max_t.append(max)
        min_t.append(min)


#データをプロットする。
fig, ax = plt.subplots()
ax.plot(days, max_t, c='red', label='max_temperature')
ax.plot(days, min_t, c='blue', label='min_temperature')
plt.fill_between(days, max_t, min_t, facecolor='blue', alpha=0.1)

#グラフのレイアウトを決める。
plt.style.use('seaborn')
plt.title('San_Francisco_Temperature', fontsize=20)
plt.xlabel('day', fontsize=15)
fig.autofmt_xdate
plt.ylabel('temperature (F)', fontsize=15)
plt.legend()

#グラフの表示
plt.show()
