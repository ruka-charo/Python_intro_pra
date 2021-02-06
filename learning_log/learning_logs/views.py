from django.shortcuts import render
from .models import Topic


def index(request):
    '''学習ノートのホームページ'''
    return render(request, 'learning_logs/index.html')


def topics(request):
    '''全てのトピックを表示する。'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
