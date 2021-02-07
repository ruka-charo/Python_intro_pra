from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline
import requests


#API呼び出しを作成してそのレスポンスを格納する。
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"ステータスコード:{r.status_code}")

#各投稿についての情報を処理する。
submission_ids = r.json()

titles, comments, texts = [], [], []

for submisson_id in submission_ids[:30]:
    #投稿ごとに、別々のAPI呼び出しを作成する。
    url = f"https://hacker-news.firebaseio.com/v0/item/{submisson_id}.json"
    r = requests.get(url)
    print(f"id: {submisson_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    #投稿ごとにデータを抽出する。
    hn_link = f"http://news.ycombinator.com/item?id={submisson_id}"
    title = response_dict['title']
    link = f"<a href='{hn_link}'>{title}</a>"

    try:
        comments.append(response_dict['descendants'])
        titles.append(title)
        texts.append(link)
    except KeyError:
        continue

#データの整理
data =[{
    'type': 'bar',
    'x': texts,
    'y': comments,
    'marker': {
        'color': 'rgb(196, 196, 196)',
        'line': {'width': 1.5, 'color': 'rgb(30, 150, 136)'}
        },
}]

my_layout = {
    'title': 'ハッカーニュースでの活発なディスカッション順',
    'xaxis': {'title': 'タイトル'},
    'yaxis': {'title': 'コメント数'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='HN_analysis.html')
