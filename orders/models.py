from django.db import models

from main.models import Shoes
from users.models import User


# Create your models here.
class OrderItemQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.product_price() for cart in self.all())

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self.all())
        return 0


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None, verbose_name='Пользователь')
    number = models.CharField(max_length=20, verbose_name='Номер телефона')
    delivery = models.BooleanField(default=False, verbose_name='Доставка')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес')
    paid = models.BooleanField(default=False, verbose_name='Метод оплаты')
    is_paid = models.BooleanField(default=False, verbose_name='Оплачено')
    status = models.BooleanField(default=False, verbose_name='Статус')

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ № {self.pk} | Заказчик {self.user.first_name} {self.user.last_name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ', related_name='order_item')
    product = models.ForeignKey(Shoes, on_delete=models.SET_DEFAULT, default=None, null=True, verbose_name='Продукт')
    name = models.CharField(verbose_name='Название')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')
    quantity = models.PositiveSmallIntegerField(verbose_name='Колличевство')

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'

    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        return round(self.price * self.quantity, 2)
