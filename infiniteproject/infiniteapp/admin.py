from django.contrib import admin
from .models import Category,Products
# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','description','image']
    prepopulated_fields = {'slug':['name']}

admin.site.register(Category,categoryadmin)

class productsadmin(admin.ModelAdmin):
    list_display = ['name','image','description','stock','availability','category']
    prepopulated_fields = {'slug':['name']}
admin.site.register(Products,productsadmin)