from django.urls import path
from . import views

app_name = 'API'

urlpatterns = [
    path('', views.ShoesAPIView.as_view(), name='index'),
    path('<int:pk>/', views.ShoesDetailAPIView.as_view(), name='detail'),
]
