from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login', views.login, name='login'),
    path('questionario', views.questionario, name='questionario'),
    path('compilazione', views.compilazione, name='compilazione'),
]