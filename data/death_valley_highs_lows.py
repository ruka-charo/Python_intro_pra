import csv
import matplotlib.pyplot as plt
from datetime import datetime


filename = 'data_sample/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #ファイルから日付と最高気温,最低気温を取得する。
    days, highs, lows = [], [], []
    for row in reader:
        day = datetime.strptime(row[2], '%Y-%m-%d')

        try:
            high = int(row[4])
            low = int(row[5])

        except ValueError:
            print(f'Missing data for {day}')
            #continue

        else:
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

title = 'Daily high and low temperatures - 2018\nDeath Valley, CA'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()
