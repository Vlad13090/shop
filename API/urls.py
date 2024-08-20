from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

app_name = 'API'

router = SimpleRouter()
router.register(r'shoes', views.ShoesViewSet)

urlpatterns = [
    path('', include(router.urls)),  # http://localhost:8000/api/shoes/  or  http://localhost:8000/api/shoes/<int:pk>/
]
