from django.contrib import admin

from orders.models import Order, OrderItem


# Register your models here.
class OrderItamInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'price', 'quantity')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery', 'status', 'paid', 'is_paid')
    search_fields = ['id']
    inlines = [OrderItamInline]
