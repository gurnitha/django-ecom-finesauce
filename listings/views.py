# listings/views.py

# # Django modules
# from django.shortcuts import render

# # Locals
# from .models import Category, Product


# # Defining View method: product_list
# def product_list(request):

#     categories 	= Category.objects.all()
#     products 	= Product.objects.all()
    
#     context = {
#     	'categories':categories,
#     	'products':products
#     }

#     return render(
#         request,
#         'product/list.html', context)


# FILTERING BY CATEGORY

# listings/views.py
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):

    categories 			= Category.objects.all()
    requested_category 	= None
    products 			= Product.objects.all()

    if category_slug:
        requested_category = get_object_or_404(
        			Category, slug=category_slug)
        products = Product.objects.filter(
        			category=requested_category)

    context = {
    	'categories':categories,
    	'requested_category':requested_category,
    	'products':products
    }

    return render(
        request,
        'product/list.html', context)


