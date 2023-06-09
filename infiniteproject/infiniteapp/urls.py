
from django.urls import path
from . import views
app_name='infiniteapp'
urlpatterns=[

    path('',views.AllProductCat,name='AllProductCat'),
    path('<slug:category_slug>/',views.AllProductCat, name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.ProductDetails,name='ProductDetails')

]