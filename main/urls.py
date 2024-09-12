from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product/<slug:slug_product>', views.DetailShoesView.as_view(), name='detail'),
    path('search/', views.IndexView.as_view(), name='search'),
]
