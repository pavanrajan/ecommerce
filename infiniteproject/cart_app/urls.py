from django.urls import path
from . import views

app_name = 'cart_app'

urlpatterns = [

    path('add/<int:product_id>/', views.Add_cart, name='cart'),
    path('', views.Cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.item_remove, name='item_remove'),
    path('delete/<int:product_id>/', views.cart_delete, name='cart_delete')
]
