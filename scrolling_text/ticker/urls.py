from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),    
]
