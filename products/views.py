from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def home(request):
    all_product = Product.objects.filter(all_product=True).order_by("-created_at")[:8]
    new = Product.objects.filter(new_arrivals=True).order_by("-created_at")[:8]
    featured = Product.objects.filter(featured=True).order_by("-created_at")[:8]
    top_selling = Product.objects.filter(top_selling=True).order_by("-created_at")[:8]
    categories = Category.objects.all()
    
    context = {
        'all_products': all_product,
        'news': new,
        'featureds': featured,
        'top_sellings': top_selling,
        'categories': categories,
    }
    return render(request, 'products/home.html', context)


def category(request,   category_id=None):
    if category_id:
        products = Product.objects.filter(categories__id=category_id).order_by('-created_at')
        category_name = Category.objects.get(id=category_id)
    else:
        products = Product.objects.all().order_by('-created_at')
        category_name = None
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_name,
    }
    return render(request, 'products/category.html', context)


