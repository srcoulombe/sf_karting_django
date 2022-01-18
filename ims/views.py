import os
import shutil 

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone 
from django.db.models import Q

from .models import InventoryItem
from .forms import InventoryItemForm

def add_new_inventory_item(request):
    if request.method == "POST":
        form = InventoryItemForm(request.POST, files=request.FILES)
        if form.is_valid():
            inventory_item = form.save(commit=False)
            inventory_item.last_updated_by = request.user
            inventory_item.last_updated_on = timezone.now()
            inventory_item.save()
            return redirect('inventory_item_details', pk=inventory_item.pk)
    else:
        form = InventoryItemForm()
    return render(request, 'ims/inventory_item_edit.html', {'form': form})

def edit_inventory_item(request, pk: int):
    inventory_item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == "POST":
        form = InventoryItemForm(request.POST, instance=inventory_item, files=request.FILES)
        if form.is_valid():
            inventory_item = form.save(commit=False)
            inventory_item.last_updated_by = request.user
            inventory_item.last_updated_on = timezone.now()
            inventory_item.save()
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

def search_inventory_items(request):
    substring = request.GET.get('q')
    items = InventoryItem.objects.filter(Q(title__contains=substring) | Q(description__contains=substring))
    return render(request, 'ims/search_results.html', {'inventoryitems': items})

def revert_database(request):
    db_directory_path = backup_db_filepath = os.path.join(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )
    active_db_filepath = os.path.join(
        db_directory_path,
        'db.sqlite3'
    )
    backup_db_filepath = os.path.join(
        db_directory_path,
        'backup_db.sqlite3'
    )
    assert os.path.isfile(backup_db_filepath)
    shutil.copyfile(
        backup_db_filepath, 
        os.path.splitext(backup_db_filepath)[0]+"_copy.sqlite3"
    )
    os.remove(active_db_filepath)
    os.rename(backup_db_filepath, active_db_filepath)
    os.rename(os.path.splitext(backup_db_filepath)[0]+"_copy.sqlite3", backup_db_filepath)
    return inventory_item_list(request)