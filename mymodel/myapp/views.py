from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def del_record(request,d):
    d=Post.objects.get(id=d)
    d.delete()
    return redirect('index') 


def create_data(request):
    if request.method =='POST':
        form = Post_form(request.POST, request.FILES)
        
        #print(form)
        if form.is_valid():
            form.save()
            # d = form.cleaned_data
            # print(d)
            # t=d['title']
            # m=d['message']
            # p=Post(title=t,text=m)
            # p.save()
            return redirect('index')
        
    else:
        form = Post_form()
        
    return render(request,'home.html',{'form':form})
def index(request):
    data=Post.objects.all()
    return render(request,'index.html',{'d':data})





def index1(request):
    


#create data\
    #Post.objects.create(title='ML',text='about making ')
    
    #or
    #p=Post(title='java',text='multipurpose language 2')
    #p.save()
    
    #filter records
    #data=Post.objects.filter(title='python programming') 
    
    # title contains
    #data=Post.objects.filter(title__contains='python')
    
    #update record
    #q=Post.objects.get(id=3)
    #q.title='DSA'
    #q.save()
    #OR
    # update record 
    #Post.objects.filter(title='Language').update(title='Java',text='java+DSA')
    
    
    #Delete record
    #i=Post.objects.get(id=2)
    #i.delete()
    
    #For AScending order 
    #Post.objects.all().order_by('title')
    data = Post.objects.all().order_by('id')
    
    #get method(fetch single  record)
    #s=Post.objects.get(title='java')
    #s=Post.objects.get(id=1) # fetch first record
    #s=Post.objects.get(id=3)  # fetch third Record 
    
    
    
    
    #fetch
    #data = Post.objects.all()
    return render(request,'index.html',{'d':data})