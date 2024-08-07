from django.shortcuts import render
from .models import Shoes


# Create your views here.
def index(request):
    products = Shoes.objects.all()
    return render(request, 'main/index.html', {'products': products})
