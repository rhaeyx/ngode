from django.urls import path

from . import views

urlpatterns = [
    path('resistor_calc/', views.index, name='index'),
]