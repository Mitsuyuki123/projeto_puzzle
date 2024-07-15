from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('02/',  views.zerotwo, name='02')
]
