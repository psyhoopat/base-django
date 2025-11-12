from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Post

class SingUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete': 'new-password',
            'placeholder': 'Введите пароль'
        }),
        strip = False,
    )
    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'autocomplete': 'new-password',
            'placeholder': 'Введите повторный пароль'
        }),
        strip=False,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите никнейм'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nickname",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите никнейм'
        }),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        }),
    )

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'cover']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя файла',
            }),
            'cover': forms.FileInput(attrs={
                'class': 'form-control',
            }),
        }
        labels = {
            'title': 'Имя файла',
            'cover': 'Фотография'
        }