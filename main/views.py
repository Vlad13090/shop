from django.shortcuts import render, get_object_or_404
from .models import Shoes


# Create your views here.
def index(request):
    products = Shoes.objects.all()
    return render(request, 'main/index.html', {'products': products})


def detail(request, slug_product):
    products = get_object_or_404(Shoes, slug=slug_product)
    return render(request, 'main/detail.html', {'products': products})


