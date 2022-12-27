from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def categories(request):
    return {'categories' : Category.objects.all()}

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products' : products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'products/details.html', {'product' : product})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category.html', {'category': category, 'products': products})