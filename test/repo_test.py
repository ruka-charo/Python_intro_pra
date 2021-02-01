import requests
from plotly.graph_objs import Bar
from plotly import offline


#API呼び出しを作成
url = 'https://api.github.com/search/repositories?q=language:Ruby&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"ステータスコード：{r.status_code}")


#結果の処理
response_dict = r.json()
repo_dict = response_dict['items']

names, stars = [], []

for repo in repo_dict:
    names.append(repo['name'])
    stars.append(repo['stargazers_count'])


#データの可視化
data = [{
    'type': 'bar',
    'x': names,
    'y': stars,

}]

my_layout = {
    'title': 'Rubyプロジェクトのスターの数について',
    'xaxis': {'title': 'プロジェクト名'},
    'yaxis': {'title': 'スターの数'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Ruby_stars.html')
