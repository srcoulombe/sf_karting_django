from django.shortcuts import render, get_object_or_404, redirect
from .models import InventoryItem
from .forms import InventoryItemForm
from django.utils import timezone 


def add_new_inventory_item(request):
    if request.method == "POST":
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            inventory_item = form.save(commit=False)
            inventory_item.last_updated_by = request.user
            inventory_item.last_updated_on = timezone.now()
            inventory_item.save()
            form.save_m2m()
            return redirect('inventory_item_details', pk=inventory_item.pk)
    else:
        form = InventoryItemForm()
    return render(request, 'ims/inventory_item_edit.html', {'form': form})

def edit_inventory_item(request, pk: int):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == "POST":
        form = InventoryItemForm(request.POST, instance=inventory_item)
        if form.is_valid():
            inventory_item = form.save(commit=False)
            inventory_item.last_updated_by = request.user
            inventory_item.last_updated_on = timezone.now()
            inventory_item.save()
            form.save_m2m()
            return redirect('inventory_item_details', pk=inventory_item.pk)
    else:
        form = InventoryItemForm(instance=inventory_item)
    return render(request, 'ims/inventory_item_edit.html', {'form': form})

def delete_inventory_item(request, pk: int):
    item = get_object_or_404(InventoryItem, pk=pk)
    item.delete()
    return inventory_item_list(request)

def inventory_item_list(request):
    items = InventoryItem.objects.order_by('last_updated_on')
    return render(request, 'ims/inventory_item_list.html', {'inventoryitems': items})

def inventory_item_details(request, pk: int):
    item = get_object_or_404(InventoryItem, pk=pk)
    return render(request, 'ims/inventory_item_details.html', {'inventoryitem': item})
