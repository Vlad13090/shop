from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import render, redirect

from carts.models import Cart
from orders.forms import OrderForm
from .models import Order, OrderItem


# Create your views here.
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.filter(user=user)

                    if cart_items.exists():
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            number=form.cleaned_data['number'],
                            delivery=form.cleaned_data['delivery'],
                            address=form.cleaned_data['address'],
                            paid=form.cleaned_data['paid'],
                        )
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )

                        # Очистить корзину после создания заказа
                        cart_items.delete()

                        return redirect('user:profile')
            except ValidationError:
                return redirect('user:profile')
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = OrderForm(initial=initial)

    return render(request, 'orders/create_order.html', {'form': form})
