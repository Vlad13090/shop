from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

app_name = 'API'

router = DefaultRouter()
router.register(r'shoes', views.ShoesViewSet, basename='shoes')

urlpatterns = [
    path('', include(router.urls)),  # http://localhost:8000/api/shoes/  or  http://localhost:8000/api/shoes/<int:pk>/
]
