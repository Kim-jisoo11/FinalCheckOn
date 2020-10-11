from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    sort = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.sort)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add = True)
    hit = models.IntegerField(default=0)

    def __str__(self):
        return '{} {}'.format(self.name, self.pub_date)


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wish_product', blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '{} // {}'.format(self.user, self.products.name)


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, )
    name = models.CharField(max_length=100, verbose_name='상품명')
    amount = models.PositiveIntegerField(verbose_name='결제금액')
    quantity = models.IntegerField(default=1)
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product')
    order_date = models.DateTimeField(auto_now_add=True)

    #모델 인스턴스를 아이디 값 내림차순 정렬
    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return '{} by {}'.format(self.products.name, self.user)