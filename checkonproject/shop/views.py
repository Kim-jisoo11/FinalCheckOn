from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Cart, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import F
import operator
# from django.db.models import Avg, Max, Min, Sum, Count

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
    
    return render(request, 'shopping.html', {'category': category, 'categories': categories ,'posts' : posts})

def cart(request):
    categories = Category.objects.all()
    cart = Cart.objects.filter(user=request.user)
    paginator = Paginator(cart, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    total_prices = 0
    for i in cart:
        print(i)
        i.products.price = i.products.price * i.quantity
        total_prices = total_prices + i.products.price    
    cart.totalAmount = total_prices
    print(cart.totalAmount)
    

    # 카테고리별 산 상품 종류 합계
    isBought = {}
    print(type(isBought))
    for i in cart:
        if i.category_id in isBought:
            sum = isBought.get(i.category_id) + 1
            isBought[i.category_id] = sum
        else:
            isBought[i.category_id] = 1

    # 구매 제품 종류 합계
    totalSum=0
    for key, value in isBought.items():
        totalSum = totalSum + value
        print(key, " : ", value)

    # 카테고리 통계
    countProduct = {}
    for i in cart:
        countProduct[i.category_id] = isBought.get(i.category_id) / totalSum * 100

    for key, value in countProduct.items():
        print(key, " : ", value)

    context = { 'cart': cart, 'categories': categories, 'posts' : posts, 'countProduct' : countProduct}

    return render(request, 'cart.html', context)

def mypage(request):
    categories = Category.objects.all()
    cart = Cart.objects.filter(user=request.user)
    
    paginator = Paginator(cart, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    total_prices = 0
    for i in cart:
        print(i)
        i.products.price = i.products.price * i.quantity
        total_prices = total_prices + i.products.price    
    cart.totalAmount = total_prices
    print(cart.totalAmount)
    

    # 카테고리별 산 상품 종류 합계
    isBought = {}
    print(type(isBought))
    for i in cart:
        if i.category_id in isBought:
            sum = isBought.get(i.category_id) + 1
            isBought[i.category_id] = sum
        else:
            isBought[i.category_id] = 1

    # 구매 제품 종류 합계
    totalSum=0
    for key, value in isBought.items():
        totalSum = totalSum + value
        print(key, " : ", value)

    # 카테고리 통계
    countProduct = {}
    def productCategory(x):
        return {1:"과일, 견과", 2:"수산", 3:"정육, 계란", 4:"채소", 5:"쌀, 잡곡", 6:"유제품", 7:"반찬, 간편식", 8:"액체류(생수, 음료, 주류)", 9:"과자, 빵", 10:"즉석조리(라면, 통조림, 소스장류)", 11:"건강식품"}[x]
    print_category = {}
    for i in cart:
        countProduct[i.category_id] = isBought.get(i.category_id) / totalSum * 100

        print_category[productCategory(i.category_id)] = countProduct.get(i.category_id)
        # 과일, 견과  : 14.28 형식으로 출력하기 위함
        # productCategory(i.caegory_id) = "과일, 견과"
        # print_category = {"과일, 견과":14.28...}

    for key, value in print_category.items():
        print(key, " : ", value)
        #출력 확인용
    for key, value in countProduct.items():
        print(key, " : ", value)
        #출력 확인용
    
    
    
    
    # sorting-> value값 기준으로 내림차순 정렬
    sortProductTuple = sorted(countProduct.items(), key=operator.itemgetter(1), reverse=True)
    firstrank = sortProductTuple[0][0]
    print(type(firstrank))
    
    # 타이틀 분류 (switch문과 비슷)
    def f(x):
        return {1:"도토리보따리 다람쥐", 2:"연어킬러 곰곰이", 3:"단백질 백만장자 고릴라", 4:"채소 요정 코끼리", 5:"방앗간도둑 참새",
                6:"얼룩얼룩 송아지", 7:"귀차니즘 나무늘보", 8:"수분부자 하마", 9:"살아있는 진저브레드 쿠키", 10:"휘리릭 냠냠 토끼", 11:"앞날창창 거북이"}[x]
    title = f(firstrank)
    print(title)

    context = {'cart': cart, 'categories': categories, 'posts' : posts, 'countProduct' : countProduct, 'title' : title, 'firstrank':firstrank, "productCategory":productCategory, "print_category":print_category}

    return render(request, 'mypage.html', context)


def delete_cart(request, product_id):
    user = request.user
    cart = Cart.objects.filter(user=request.user)
    quantity = 0
    
    if request.method == 'POST':
        try:
            pk = request.POST.get('product')
            product = Product.objects.get(pk=pk)
            for i in cart:
                if i.products == product :
                    quantity =  i.quantity
            if quantity > 0 :
                product = Product.objects.filter(pk=pk)
                cart = Cart.objects.filter(user=request.user, products__in=product)
                cart.delete()
                return redirect('cart')
        except:
            return redirect('cart')

@login_required
def cart_or_buy(request, product_id):
    quantity = request.POST.get('quantity', '')
    product = Product.objects.get(pk=product_id)
    user = request.user
    categories = Category.objects.all()
    category = product.category
    initial = {'name': product.name, 'amount': product.price, 'quantity': quantity, 'category':product.category}
    cart = Cart.objects.filter(user=user)
    if request.method == 'POST':
        if 'add_cart' in request.POST:
            for i in cart :
                if i.products == product:
                    product = Product.objects.filter(pk=product_id)
                    Cart.objects.filter(user=request.user, products__in=product).update(quantity=F('quantity') + quantity)
                    messages.success(request,'장바구니 등록 완료')
                    return redirect('shopping', category.pk)
            Cart.objects.create(user=user, products=product, quantity=quantity, category=category)
            return redirect('shopping', category.pk)
        

