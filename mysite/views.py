from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login

from mysite.forms import SingUpForm, LoginForm

# Create your views here.
def index(request):
    context = {
        "username": "admin",
        "is_auth": request.user.is_authenticated,
        "links_not_auth": {
            "register": "Регистрация",
            "login": "Войти",
        },
        "links_auth": {
            "profile": "Профиль",
        }
    }
    return render(request, "page/main.html", context)

def register(request):
    # https://fixmypc.ru/post/sozdaem-stranitsu-registratsii-polzovatelei-django/?ysclid=mhsztne413664128872
    if request.method == "POST":
        form = SingUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]

            user = User.objects.create_user(username=username, email=email, password=password)

            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # form.save()

            return HttpResponseRedirect("/login")
    else:
        form = SingUpForm()

    return render(request, "page/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/profile")
            else:
                return render(request, "page/login.html", {"form": form})
    else:
        form = LoginForm()

    return render(request, "page/login.html", {"form": form})

@login_required
def profile(request):
    return render(request, "page/profile.html")

def load_image(request):
    return HttpResponse("Page load image.")

def logout_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/login")

    logout(request)
    return HttpResponseRedirect("/login")