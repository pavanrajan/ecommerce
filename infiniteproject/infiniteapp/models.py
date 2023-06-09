from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='category',blank=True)
    slug=models.SlugField(unique=True,max_length=100)

    class Meta:
        ordering=['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('infiniteapp:products_by_category',args=[self.slug])

    def __str__(self):
        return'{}'.format (self.name)

class Products(models.Model):
    name=models.CharField(max_length=100,unique=True)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    availability=models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    slug=models.SlugField(unique=True)
    stock=models.IntegerField()
    image=models.ImageField(upload_to='products',blank=None)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('infiniteapp:ProductDetails', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.name)

