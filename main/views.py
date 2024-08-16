from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Shoes
from .utils import g_search


# Create your views here.
# def index(request):
#     order_by = request.GET.get('order_by', None)
#     on_sale = request.GET.get('on_sale', None)
#     page = request.GET.get('page', 1)
#     query = request.GET.get('q', None)
#
#     if query:
#         products = g_search(query)
#     else:
#         products = Shoes.objects.all()
#
#     if on_sale:
#         products = products.filter(sell__gt=0)
#
#     if order_by and order_by != 'default':
#         products = products.order_by(order_by)
#
#     paginator = Paginator(products, 6)  # Инициализируем пагинатор и определяем кол-во продуктов
#     current_page = paginator.page(page)  # Текущая страница
#
#     return render(request, 'main/index.html', {'products': current_page})

class IndexView(ListView):
    template_name = 'main/index.html'
    context_object_name = 'products'
    paginate_by = 6
    allow_empty = True  # Разрешение для отображения пустой страницы

    def get_queryset(self):
        # category_slug = self.kwargs.get('slug_product')
        order_by = self.request.GET.get('order_by', None)
        on_sale = self.request.GET.get('on_sale', None)
        query = self.request.GET.get('q', None)

        if query:
            products = g_search(query)
        else:
            products = Shoes.objects.all()

        if on_sale:
            products = products.filter(sell__gt=0)

        if order_by and order_by != 'default':
            products = products.order_by(order_by)

        return products


# def detail(request, slug_product):
#     products = get_object_or_404(Shoes, slug=slug_product)
#     return render(request, 'main/detail.html', {'products': products})

class DetailShoesView(DetailView):
    template_name = 'main/detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return get_object_or_404(Shoes, slug=self.kwargs['slug_product'])
