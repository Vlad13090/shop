from django.shortcuts import render, redirect

from carts.models import Cart
from main.models import Shoes


# Create your views here.
def cart_add(request, product_slug):
    product = Shoes.objects.get(slug=product_slug)
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
    return redirect(request.META['HTTP_REFERER'])


def cart_plus(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    cart.quantity += 1
    cart.save()
    return redirect(request.META['HTTP_REFERER'])


def cart_minus(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    cart.quantity -= 1
    cart.save()
    return redirect(request.META['HTTP_REFERER'])


def cart_remove(request, product_id):
    cart = Cart.objects.get(id=product_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER'])
