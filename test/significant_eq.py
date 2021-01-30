import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


#ファイルからデータを読み取る
filename = '/Users/rukaoide/Library/Mobile Documents/\
com~apple~CloudDocs/Documents/Python/Python_intro_pra/\
data/data_sample/significant_eq_month_readable.json'

with open(filename) as f:
    all_eq_data = json.load(f)


#個別データをリスト化
eq_data_list = all_eq_data['features']

#mag, lon, lat, hover_textの情報を抽出
mags, lons, lats, hover_texts = [], [], [], []

for eq_data in eq_data_list:
    mags.append(eq_data['properties']['mag'])
    lons.append(eq_data['geometry']['coordinates'][0])
    lats.append(eq_data['geometry']['coordinates'][1])
    hover_texts.append(eq_data['properties']['title'])


#データをまとめる
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'マグニチュード'},
    }
}]

my_layout = Layout(title=all_eq_data['metadata']['title'])


#データの表示
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='significant_earthquakes.html')
