# listings/views.py

# Django modules
from django.shortcuts import render

# Locals
from .models import Category, Product


# Defining View method: product_list
def product_list(request):

    categories 	= Category.objects.all()
    products 	= Product.objects.all()
    
    context = {
    	'categories':categories,
    	'products':products
    }

    return render(
        request,
        'product/list.html', context)
