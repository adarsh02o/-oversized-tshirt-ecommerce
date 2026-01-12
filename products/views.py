from django.shortcuts import render, get_object_or_404
from .models import TShirt

def home(request):
    tshirts = TShirt.objects.filter(is_oversized=True)[:6]
    context = {
        'tshirts': tshirts,
    }
    return render(request, 'products/home.html', context)

def product_list(request):
    tshirts = TShirt.objects.filter(is_oversized=True)
    context = {
        'tshirts': tshirts,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    tshirt = get_object_or_404(TShirt, pk=pk)
    context = {
        'tshirt': tshirt,
    }
    return render(request, 'products/product_detail.html', context)
