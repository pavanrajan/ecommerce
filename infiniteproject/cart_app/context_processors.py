from .models import Cart,Cart_Item
from .views import Cart_ID

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id=Cart_ID(request))
            cart_item=Cart_Item.objects.all().filter(cart=cart[:1])
            for cart_items in cart_item:
                item_count += cart_items.quantity
        except Cart.DoesNotExist:
            item_count=0
    return dict(item_count=item_count)