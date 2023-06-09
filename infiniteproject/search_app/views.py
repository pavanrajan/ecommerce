from django.shortcuts import render
from infiniteapp .models import Products
from django.db.models import Q
# Create your views here.
def Search(request):
    query=None
    result=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        result=Products.objects.all().filter(Q(name__contains=query)|Q(description__contains=query))

    return render(request,'search.html',{'query':query,'result':result})