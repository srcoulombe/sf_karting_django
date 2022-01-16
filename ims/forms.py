from ast import In
from django import forms
from .models import InventoryItem

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ('title', 'description', 'on_hold', 'in_stock', 'price', 'restocking_cost')
