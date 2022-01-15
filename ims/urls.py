from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.inventory_item_list, name='inventory_item_list'),
]