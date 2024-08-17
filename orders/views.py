from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from carts.models import Cart
from orders.forms import OrderForm
from .models import Order, OrderItem


# Create your views here.
# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     user = request.user
#                     cart_items = Cart.objects.filter(user=user)
#                     if cart_items.exists():
#                         order = Order.objects.create(
#                             user=user,
#                             number=form.cleaned_data['number'],
#                             delivery=form.cleaned_data['delivery'],
#                             address=form.cleaned_data['address'],
#                             paid=form.cleaned_data['paid'],
#                         )
#                         for cart_item in cart_items:
#                             product = cart_item.product
#                             name = cart_item.product.name
#                             price = cart_item.product.sell_price()
#                             quantity = cart_item.quantity
#
#                             OrderItem.objects.create(
#                                 order=order,
#                                 product=product,
#                                 name=name,
#                                 price=price,
#                                 quantity=quantity,
#                             )
#                         cart_items.delete()
#
#                         return redirect('user:profile')
#             except ValidationError:
#                 return redirect('user:profile')
#     else:
#         initial = {
#             'first_name': request.user.first_name,
#             'last_name': request.user.last_name,
#         }
#         form = OrderForm(initial=initial)
#
#     return render(request, 'orders/create_order.html', {'form': form})


class CreateOrderView(LoginRequiredMixin, FormView):
    template_name = 'orders/create_order.html'
    form_class = OrderForm
    success_url = reverse_lazy('user:profile')

    def get_initial(self):
        initial = super().get_initial()
        initial['first_name'] = self.request.user.first_name
        initial['last_name'] = self.request.user.last_name
        return initial

    def form_valid(self, form):
        try:
            with transaction.atomic():
                user = self.request.user
                cart_items = Cart.objects.filter(user=user)

                if cart_items.exists():
                    order = Order.objects.create(
                        user=user,
                        number=form.cleaned_data['number'],
                        delivery=form.cleaned_data['delivery'],
                        address=form.cleaned_data['address'],
                        paid=form.cleaned_data['paid'],
                    )
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
                    cart_items.delete()

                    return redirect('user:profile')
        except ValidationError:
            return redirect('user:profile')
