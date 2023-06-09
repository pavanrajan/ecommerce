from logging import exception

from django.shortcuts import render, get_object_or_404
from .models import Category,Products
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def AllProductCat(request, category_slug=None):
    c_page=None
    product_list=None
    if category_slug!= None:
        c_page=get_object_or_404(Category,slug=category_slug)
        product_list=Products.objects.all().filter(category=c_page, availability=True)
    else:
       product_list= Products.objects.all().filter(availability=True)
    paginator = Paginator(product_list,3)
    try :
        page=int(request.GET.get('page','1'))
    except :
        page=1
    try:
        product=paginator.page(page)
    except (InvalidPage,EmptyPage):
        product=paginator.page(paginator.num_pages)
    return render(request,'home.html',{'category':c_page,'product':product})
def ProductDetails(request,category_slug,product_slug):
    try :
        product=Products.objects.get(category__slug=category_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})
