from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:product_slug>', views.cart_add, name='cart_add'),
    path('cart_remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart_plus/<int:cart_id>', views.cart_plus, name='cart_plus'),
    path('cart_minus/<int:cart_id>', views.cart_minus, name='cart_minus'),
]
