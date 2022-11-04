from django.shortcuts import render,redirect
from .models import *
# from secondapp.forms import *
from secondapp.forms import *

# Create your views here.
def index(request):
    data=student.objects.all()
    return render(request,'f1.html',{'data':data})
def del_record(request,d):
    s1=student.objects.get(id=d)
    s1.delete()
    return redirect('app1:first_page')

def edit_record(request,d):
    s1=student.objects.get(id=d)
    if request.method=='POST':
        form=student_form(request.POST,instance=s1)
        if form.is_valid():
            form.save()
            return redirect('app1:first_page')
    else:
        form = student_form(instance=s1)
        # if form.is_valid():
        #     return redirect('f1')
    return render(request,'edit.html',{'form':form})