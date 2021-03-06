from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<slug:category_slug>/', views.home, name='products_by_category'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail') 
]