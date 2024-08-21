from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter


router = DefaultRouter()
router.register(r'shoes', views.ShoesViewSet, basename='shoes')

urlpatterns = [
    path('', include(router.urls)),  # http://localhost:8000/api/shoes/  or  http://localhost:8000/api/shoes/<int:pk>/
    path('auth/', include('rest_framework.urls')),
]
