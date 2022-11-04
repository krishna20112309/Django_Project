from django.shortcuts import render
from django.http import *
import datetime

# Create your views here.
def index(request):   #HttpRequest
    #data = {}
    #data ={'name': 'Krishna', 'address':'d', 'salary':2000}  
    emp=[
        {'name': 'Krishna', 'address':'d', 'salary':2000},
        {'name': 'jyoti', 'address':'d', 'salary':250050},
        {'name': 'Raj', 'address':'d', 'salary':205000}] 
       
    #return HttpResponse('Hello Krishna jaiswal')
    return render(request,'index.html',{'d':emp})
def second(request):
    return render(request,'home.html')