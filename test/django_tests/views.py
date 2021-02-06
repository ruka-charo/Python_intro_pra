from django.shortcuts import render


def index(request):
    '''Piizariaプロジェクトのホームページ'''
    return render(request, 'django_tests/index.html')
