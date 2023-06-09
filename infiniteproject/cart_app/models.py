from django.db import models
from infiniteapp.models import Products, Category


# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering=['date_added']
    def __str__(self):
        return '{}'.format(self.cart_id)
class Cart_Item(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0,blank=True)
    active=models.BooleanField(default=True)

    class Meta:
        db_table='Cart_Item'

    def subtotal(self):
        return self.product.price * self.quantity
    def __str__(self):
        return '{}'.format(self.product)
