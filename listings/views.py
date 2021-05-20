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

# Django modules
from django.shortcuts import (
            render, get_object_or_404, redirect)

# Locals
from listings.models import Category, Product, Review
from listings.forms import ReviewForm


# Product list
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


# # Product detail
# def product_detail(request, category_slug, product_slug):

#     category = get_object_or_404(
#     		Category, slug=category_slug)
#     product = get_object_or_404(
# 	        Product,
# 	        category_id = category.id,
# 	        slug=product_slug
#     )

#     context = {
#     	'product':product,
#     }

#     return render(
#         request,
#         'product/detail.html', context
#     )

# Product detail + review
def product_detail(request, category_slug, product_slug):

    category = get_object_or_404(
            Category, slug=category_slug)
    product = get_object_or_404(
            Product,
            category_id = category.id,
            slug=product_slug
    )

    if request.method == 'POST':

        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            cf = review_form.cleaned_data
            author_name = "Anonymous"
            Review.objects.create(
                product = product,
                author = author_name,
                rating = cf['rating'],
                text = cf['text']
            )

        return redirect(
                'listings:product_detail',
                category_slug=category_slug, 
                product_slug=product_slug)
    
    else:

        review_form = ReviewForm()
        return render(
            request,
            'product/detail.html',
            {
                'product': product,
                'review_form': review_form
            }
        )