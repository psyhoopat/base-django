from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
    context = {
        "username": "admin",
        "is_auth": False,
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # first_name = form.cleaned_data["first_name"]
            # last_name = form.cleaned_data["last_name"]
            # email = form.cleaned_data["email"]
            # password = form.cleaned_data["password"]
            #
            # user = User.objects.create_user(first_name, email, password)
            #
            # user.last_name = first_name
            # user.last_name = last_name
            # user.save()
            form.save()

            return HttpResponseRedirect("/login")
    else:
        form = UserCreationForm()

    return render(request, "page/register.html", {"form": form})

def login(request):
    return render(request, "page/login.html")

def profile(request):
    return render(request, "page/profile.html")

def load_image(request):
    return HttpResponse("Page load image.")