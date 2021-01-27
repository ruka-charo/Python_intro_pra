import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data_sample/sitka_weather_2018_simple.csv'


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    '''何行目に何の項目があるか確認する。
    for index, column_header in enumerate(header_row):
        print(index, column_header)'''

    #ファイルから日付と最高気温,最低気温を取得する。
    days, highs, lows = [], [], []
    for row in reader:
        day = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        days.append(day)
        highs.append(high)
        lows.append(low)


#最高気温のグラフを描画する。
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(days, highs, c='red')
ax.plot(days, lows, c='blue')
plt.fill_between(days, highs, lows, facecolor='blue', alpha=0.1)

#グラフにフォーマットを指定する(どちらでも良い)。
'''
ax.set_title('Daily high and low tenperatures, July 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
'''
plt.title('Daily high tenperatures - 2018', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()
