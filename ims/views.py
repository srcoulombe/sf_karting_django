from django.shortcuts import render

# Create your views here.

def inventory_item_list(request):
    return render(request, 'ims/inventory_item_list.html', {})