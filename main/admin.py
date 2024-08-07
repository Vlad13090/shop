from django.contrib import admin

from main.models import Shoes, Category


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'slug', 'category', 'sell')

    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
