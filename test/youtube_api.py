from apiclient.discovery import build

YOUTUBE_API_KEY = 'AIzaSyAzRcfc-LtfQ7MBvorjeFnMtZzz1GLGKZg'

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part='snippet',
    #検索したい文字列を指定
    q='Macbook pro',
    #視聴回数が多い順に取得
    order='viewCount',
    type='video',
).execute()

search_response['items'][:3]
