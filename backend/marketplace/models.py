from django.db import models
from general.models import UserDetails
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    Name    =   models.CharField(max_length=150)
    Desc    =   models.TextField(default="")
    Img     =   models.ImageField()
    Company =   models.CharField(max_length=150)
    Stock   =   models.CharField(max_length=10)
    Created =   models.DateTimeField(timezone.now)
    Price   =   models.CharField(max_length=10)
    Type    =   models.CharField(max_length=10,default="New")   # Recycled or Fresh Arrival
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = "Product"
        verbose_name_plural=verbose_name

class Cart(models.Model):
    User    =   models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING)
    Prod_Id =   models.ManyToManyField(Product)
    Qty     =   models.CharField(max_length=10)
    class Meta:
        verbose_name = "Cart"
        verbose_name_plural=verbose_name

class Wishlist(models.Model):
    User    =   models.ForeignKey(UserDetails,on_delete=models.DO_NOTHING)
    Prod_Id =   models.ManyToManyField(Product)
    class Meta:
        verbose_name = "WishList"
        verbose_name_plural=verbose_name
