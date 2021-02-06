'''django_testsのURLパターンの定義'''


from django.urls import path
from . import views


app_name = 'django_tests'
urlpatterns = [
        #ホームページ
        path('', views.index, name='index'),
]
