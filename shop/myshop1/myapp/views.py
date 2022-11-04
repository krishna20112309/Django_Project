from django.shortcuts import render
from .models import *
from django.http import *
from .forms import *

# Create your views here.
def index(request):
    p=Product.objects.all()
    return render(request,'index.html',{'p':p})

def view(request,d):
    z=Product.objects.get(id=d)
    return render(request,'view.html',{'z':z})

def cart_items(request,d):
    if request.method=='POST':
        x=Product.objects.get(id=d)
        form=cart_form(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.pro_info=x
            q1=int(request.POST.get('q'))
            print(x.price,q1)
            f.total_price=x.price*q1
            f.save()
            return HttpResponse('item added to cart')
            