from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'index.html')

def show_category(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category).order_by('pub_date')
    lank_products = Product.objects.filter(category=category).order_by('-hit')[:4]
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    
    return render(request, 'shopping.html', {'lank_products': lank_products, 'products': products, 'category': category, 'categories': categories ,'posts' : posts})

