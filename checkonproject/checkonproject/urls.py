"""checkonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('shopping/<int:category_id>/', views.show_category, name='shopping'),
    path('accounts/login/', accounts.views.login, name ='login'),
    path('login/',accounts.views.login, name = 'login'),
    path('logout/',accounts.views.logout, name = 'logout'),
    path('signup/',accounts.views.signup, name = 'signup'),
    path('<int:product_id>/cart_or_buy/', views.cart_or_buy, name='cart_or_buy'),
    path('cart/', views.cart, name='cart'),
    path('delete/<int:product_id>/', views.delete_cart, name='delete_cart'),
    path('mypage/', views.mypage, name = 'mypage'),
    path('mypageExcept/', views.mypage, name='mypageExcept'),
    path('shopping/1/login/', accounts.views.login, name ='login'),
    path('shopping/2/login/', accounts.views.login, name ='login'),
    path('shopping/3/login/', accounts.views.login, name ='login'),
    path('shopping/4/login/', accounts.views.login, name ='login'),
    path('shopping/5/login/', accounts.views.login, name ='login'),
    path('shopping/6/login/', accounts.views.login, name ='login'),
    path('shopping/7/login/', accounts.views.login, name ='login'),
    path('shopping/8/login/', accounts.views.login, name ='login'),
    path('shopping/9/login/', accounts.views.login, name ='login'),
    path('shopping/10/login/', accounts.views.login, name ='login'),
    path('shopping/11/login/', accounts.views.login, name ='login'),



    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

