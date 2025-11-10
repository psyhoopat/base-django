from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/image/', views.load_image, name='load_image'),
    path('logout/', views.logout_view, name='logout'),
]