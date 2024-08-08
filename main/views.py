from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Shoes
from .utils import g_search


# Create your views here.
def index(request):
    order_by = request.GET.get('order_by', None)
    on_sale = request.GET.get('on_sale', None)
    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)

    if query:
        products = g_search(query)
    else:
        products = Shoes.objects.all()

    if on_sale:
        products = products.filter(sell__gt=0)

    if order_by and order_by != 'default':
        products = products.order_by(order_by)

    paginator = Paginator(products, 6)  # Инициализируем пагинатор и определяем кол-во продуктов
    current_page = paginator.page(page)  # Текущая страница

    return render(request, 'main/index.html', {'products': current_page})


def detail(request, slug_product):
    products = get_object_or_404(Shoes, slug=slug_product)
    return render(request, 'main/detail.html', {'products': products})
