from django.shortcuts import render
from .models import Pizza, Topping


def index(request):
    '''Piizariaプロジェクトのホームページ'''
    return render(request, 'django_tests/index.html')


def pizzas(request):
    '''ピザの一覧を表示する。'''
    pizzas = Pizza.objects.order_by('date_added')
    context = {'pizzas': pizzas}
    return render(request, 'django_tests/pizzas.html', context)


def pizza(request, pizza_id):
    '''トッピングページを表示する。'''
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'django_tests/pizza.html', context)
