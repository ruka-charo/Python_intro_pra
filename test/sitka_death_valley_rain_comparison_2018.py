import csv
import matplotlib.pyplot as plt
from datetime import datetime


#csvファイルからデータを読み取る。
filename_sitka = '/Users/rukaoide/Library/Mobile Documents/\
com~apple~CloudDocs/Documents/Python/Python_intro_pra/\
data/data_sample/sitka_weather_2018_simple.csv'

filename_valley = '/Users/rukaoide/Library/Mobile Documents/\
com~apple~CloudDocs/Documents/Python/Python_intro_pra/\
data/data_sample/death_valley_2018_simple.csv'

with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #ファイルから日付とsitkaの降水量のデータを抜き出す。
    days, sitka_rains = [], []

    for row in reader:
        day_1 = datetime.strptime(row[2], '%Y-%m-%d')
        sitka_rain = float(row[3])
        days.append(day_1)
        sitka_rains.append(sitka_rain)

with open(filename_valley) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #ファイルからdeath_valleyの降水量のデータを抜き出す。
    days_2, valley_rains = [], []

    for row in reader:
        day_2 = datetime.strptime(row[2], '%Y-%m-%d')
        valley_rain = float(row[3])
        days_2.append(day_2)
        valley_rains.append(valley_rain)


#データをグラフに入れる。
fig, ax = plt.subplots()
ax.plot(days, sitka_rains, c='red', label='sitka')
ax.plot(days_2, valley_rains, c='blue', label='death_valley')

#グラフのレイアウトを決める。
plt.style.use('seaborn')
plt.legend()
plt.title('sitka_valley_rains_comparison', fontsize=15)
plt.xlabel('day', fontsize=15)
fig.autofmt_xdate()
plt.ylabel('rain', fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=15)

#グラフの表示
plt.show()
