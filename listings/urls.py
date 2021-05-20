# listings/urls.py

# Django modules
from django.urls import path

# Locals
from listings import views

app_name = 'listings'

urlpatterns = [
    path('', views.product_list, name='product_list'),
]