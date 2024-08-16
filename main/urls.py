from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug:slug_product>', views.DetailShoesView.as_view(), name='detail'),
    path('search/', views.index, name='search'),
    # path('user_cart/', views.user_cart, name='user_cart'),
]
