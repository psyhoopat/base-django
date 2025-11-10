from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User

from mysite.forms import SingUpForm


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

def login(request):
    return render(request, "page/login.html")

def profile(request):
    return render(request, "page/profile.html")

def load_image(request):
    return HttpResponse("Page load image.")