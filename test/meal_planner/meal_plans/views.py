from django.shortcuts import render


def index(request):
    '''食事計画のホームページ'''
    return render(request, 'meal_plans/index.html')
