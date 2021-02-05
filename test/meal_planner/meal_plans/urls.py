'''meal_plansのURLパターンの定義'''

from django.urls import path
from . import views


app_name = 'meal_plans'
urlpatterns = [
        #ホームページ
        path('', views.index, name='index'),
]
