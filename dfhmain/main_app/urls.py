import django
from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
]

