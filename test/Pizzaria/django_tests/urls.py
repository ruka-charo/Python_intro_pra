'''django_testsのURLパターンの定義'''


from django.urls import path
from . import views


app_name = 'django_tests'
urlpatterns = [
        #ホームページ
        path('', views.index, name='index'),
        #ピザ一覧ページ
        path('pizzas/', views.pizzas, name='pizzas'),
        #トッピングページ
        path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]
