from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Shoes


# Create your views here.
def index(request, page=1):
    products = Shoes.objects.all()

    paginator = Paginator(products, 3)  # Инициализируем пагинатор и определяем кол-во продуктов
    current_page = paginator.page(page)  # Текущая страница

    return render(request, 'main/index.html', {'products': current_page})


def detail(request, slug_product):
    products = get_object_or_404(Shoes, slug=slug_product)
    return render(request, 'main/detail.html', {'products': products})
