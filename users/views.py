from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

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


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.instance
#             auth.login(request, user)
#             # messages.success(request, 'Вы успешно зарегистрировались')
#             return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'users/registration.html', {'form': form})


class UserRegistrationView(CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        user = form.instance
        if user:
            form.save()
            auth.login(self.request, user)
        return HttpResponseRedirect(self.success_url)


@login_required
def logout(request):
    # messages.success(request, 'Вы вышли из аккаунта')
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             # messages.success(request, 'Профиль обновлен')
#             return HttpResponseRedirect(reverse('user:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#
#     orders = (
#         Order.objects.filter(user=request.user)
#         .prefetch_related(
#             Prefetch(
#                 'order_item',
#                 queryset=OrderItem.objects.select_related('product'),
#             )
#         ).order_by('-id')
#     )
#     return render(request, 'users/profile.html', {"form": form, "orders": orders})

class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = (
            Order.objects.filter(user=self.request.user)
            .prefetch_related(
                Prefetch(
                    'order_item',
                    queryset=OrderItem.objects.select_related('product'),
                )
            ).order_by('-id')
        )
        return context
