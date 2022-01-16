from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.inventory_item_list, name='inventory_item_list'),
    path('inventoryitem/<int:pk>/', views.inventory_item_details, name='inventory_item_details'),
    path('inventoryitem/<int:pk>/delete', views.delete_inventory_item, name='delete_inventory_item'),
    path('inventoryitem/add_new_inventory_item/', views.add_new_inventory_item, name='add_new_inventory_item'),
    path('inventoryitem/<int:pk>/edit/', views.edit_inventory_item, name='edit_inventory_item'),
    path('search/', views.search_inventory_items, name='search_results'),
    
]