import csv
import datetime
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


filename = '/Users/rukaoide/Library/Mobile Documents/\
com~apple~CloudDocs/Documents/Python/Python_intro_pra/\
data/data_sample/MODIS_C6_Global_24h.csv'

#csvからデータの取り出し
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, row in enumerate(header_row):
        if row == 'latitude':
            index_lat = index
        elif row == 'longitude':
            index_lon = index
        elif row == 'brightness':
            index_bright = index
        elif row == 'acq_time':
            index_time = index

    #必要データの抜き出し
    lats, lons, brights, times, texts = [], [], [], [], []

    for row in reader:
        time = row[index_time]
        bright = row[index_bright]
        label = f'{time}-{bright}'
        lats.append(row[index_lat])
        lons.append(row[index_lon])
        brights.append(float(bright))
        times.append(time)
        texts.append(label)


#データをまとめる
data = [{
    'type': 'scattergeo',
    'lat': lats,
    'lon': lons,
    'text': texts,
    'marker': {
        'size': [bright/40 for bright in brights],
        'color': brights,
        'colorscale': 'YlOrRd',
        'reversescale': True,
        'colorbar': {'title': '火事の明るさ'},
    }
}]

my_layout = Layout(title=str(datetime.date(2021, 1, 28)) + '\tworld_fires')

#データのプロット
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='2021_1_28_world_fires.html')
