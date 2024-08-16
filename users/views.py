from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from orders.models import Order, OrderItem
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


# Create your views here.
# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 # messages.success(request, f'Добро пожаловать, {username}')
#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserLoginForm()
#
#     return render(request, 'users/login.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('main:index')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            # messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


@login_required
def logout(request):
    # messages.success(request, 'Вы вышли из аккаунта')
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Профиль обновлен')
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    orders = (
        Order.objects.filter(user=request.user)
        .prefetch_related(
            Prefetch(
                'order_item',
                queryset=OrderItem.objects.select_related('product'),
            )
        ).order_by('-id')
    )
    return render(request, 'users/profile.html', {"form": form, "orders": orders})
