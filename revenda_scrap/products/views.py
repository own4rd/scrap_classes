from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator

def product_list(request):
    product_list = Product.objects.all().order_by('-created_at')
    paginator = Paginator(product_list, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    parcel_value = product.price / 3
    context = {
        'product': product,
        'parcel_value': parcel_value,
    }
    return render(request, 'products/product_detail.html', context)
