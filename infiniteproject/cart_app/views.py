from django.shortcuts import render, redirect, get_object_or_404
from infiniteapp.models import Products, Category
from .models import Cart,Cart_Item
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def Cart_ID(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
def Add_cart(request,product_id):
    product=Products.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=Cart_ID(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=Cart_ID(request))
        cart.save()
    try:
        cart_item=Cart_Item.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except Cart_Item.DoesNotExist:
        cart_item=Cart_Item.objects.create(cart=cart,product=product,quantity=1)
        cart_item.save()
    return redirect('cart_app:cart_detail')
def Cart_detail(request,total=0,counter=0,cart_item=None):
    try:
        cart=Cart.objects.get(cart_id=Cart_ID(request))
        cart_item=Cart_Item.objects.filter(cart=cart,active=True)
        for cart_items in cart_item:
            total += (cart_items.product.price * cart_items.quantity)
            counter += cart_items.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'cart_item':cart_item,'total':total,'counter':counter})

def item_remove(request,product_id):
    cart=Cart.objects.get(cart_id=Cart_ID(request))
    product=get_object_or_404(Products,id=product_id)
    cart_items=Cart_Item.objects.get(cart=cart,product=product)
    if cart_items.quantity > 1:
        cart_items.quantity -= 1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cart_app:cart_detail')
def cart_delete(request,product_id):
    cart=Cart.objects.get(cart_id=Cart_ID(request))
    product=get_object_or_404(Products,id=product_id)
    cart_items=Cart_Item.objects.get(cart=cart,product=product)
    cart_items.delete()
    return redirect('cart_app:cart_detail')

