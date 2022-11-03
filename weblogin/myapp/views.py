from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import *
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.http import require_http_methods

# Create your views here.
def user_login(request):
    return render(request,'login.html')

@require_http_methods("POST")

def user_auth(request):
    #if request.method=="POST"
        u=request.POST.get('username')
        p=request.POST.get('password')
        
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('login')
        else:
            return HttpResponse('Invalid username and password ')
#for change the url after login
def home(request):
    if request.user.is_authenticated:
        return index_page(request)
    else:
        return user_login(request)
def detail_post(request,d):
    z=Post.objects.get(id=d)
    return render(request,'detail.html',{'z':z})    
          
def index_page(request):
   
    if request.method=='POST':
        form=Post_form(request.POST)
        if form.is_valid():
            f1=form.save(commit=False)
            f1.user = request.user
            f1.save()
            return redirect('login')
    else:
        form=Post_form()
        data=Post.objects.all()
    return render(request,'index.html',{'form':form,'data':data})        
        
def user_logout(request):
    logout(request)
    return redirect('login')   
def delete(request,d):
    z=Post.objects.get(id=d)
    z.delete()
    return redirect('login')              
        
def user_reg(request):
    if request.method =='POST':
        form=reg_form(request.POST)
        if form.is_valid():
            d=form.cleaned_data
            u=d['username']
            e=d['email']
            p=d['password']
            
            User.objects.create_user(username=u,email=e,password=p)
            return redirect('login')
    else:
        form = reg_form()
        return render(request,'reg.html',{'form':form})