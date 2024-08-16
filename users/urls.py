from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]
