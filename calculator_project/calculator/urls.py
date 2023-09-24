# calculator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name='calculator'),
        path('get_calculator/', views.get_calculator, name='get_calculator'),

]
