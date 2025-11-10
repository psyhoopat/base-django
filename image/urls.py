from django.urls import path
from . import views

urlpatterns = [
    path('load/', views.load_image, name='load_image'),
]