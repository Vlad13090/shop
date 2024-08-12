from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'class': 'form-control',
                                      })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password',
                                          'class': 'form-control',
                                          })
    )

    class Meta:
        model = User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'username', 'email')

    image = forms.ImageField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
