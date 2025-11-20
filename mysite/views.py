from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from mysite.forms import SingUpForm, LoginForm
from .forms import PostForm

from .models import Post

# Create your views here.
def index(request):
    # передать статус аутентифицированного юзера
    context = {
        "username": "admin",
        "is_auth": request.user.is_authenticated,
    }

    return render(request, "page/main.html", context)

def register(request):
    # как создать регистрацию: https://fixmypc.ru/post/sozdaem-stranitsu-registratsii-polzovatelei-django/?ysclid=mhsztne413664128872

    # если пользователь аутентифицирован перенаправим на страницу профиля
    if request.user.is_authenticated:
        return HttpResponseRedirect("/profile")

    if request.method == "POST":
        form = SingUpForm(request.POST) # передать данные в форму
        if form.is_valid():
            # получаем данные
            username = form.cleaned_data['username']
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            # получить юзера из модели
            user = User.objects.create_user(username=username, email=email, password=password)

            # добавим значения и сохраним в базу данных
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # редирект на логин
            return HttpResponseRedirect("/login")
    else:
        form = SingUpForm() # создать обычную форму

    context = { "form": form }
    return render(request, "page/register.html", context)

def login_view(request):

    # если пользователь аутентифицирован перенаправим на страницу профиля
    if request.user.is_authenticated:
        return HttpResponseRedirect("/profile")

    if request.method == "POST":
        form = LoginForm(data=request.POST or None)
        if form.is_valid():
            # получить данные
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # аутентификация
            user = authenticate(username=username, password=password)

            # проверка на аутентификацию
            if user is not None:
                login(request, user) # войти
                return HttpResponseRedirect("/profile")
            else:
                # пользователь не определен
                return render(request, "page/login.html", {
                    "form": form,
                    "error": True,
                    "message": "Неправильный пользователь и/или пароль."
                })
    else:
        form = LoginForm() # создать форму

    context = { "form": form }
    return render(request, "page/login.html", context)

@login_required
def profile(request):
    object_list = Post.objects.filter(user_id=request.user.id) # только пользовательские картинки

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # получить данные
            title = form.cleaned_data["title"]
            cover = form.cleaned_data["cover"]

            # получить пользователя и создать новую картинку
            user = User.objects.get(pk=request.user.pk)
            obj = Post.objects.create(title=title, cover=cover, user_id=user)
            obj.save()

            return HttpResponseRedirect("/profile")
    else:
        form = PostForm() # создать форму

    context = {
        "is_auth": request.user.is_authenticated,
        "user": request.user,
        "form": form,
        "object_list": object_list,
    }

    return render(request, "page/profile.html", context)

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")