
from django.shortcuts import render, redirect
from secondapp.forms import student_form

# Create your views here.
def page2(request):
    if request.method=='POST':
        form=student_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app1:first_page')
    else:
        form = student_form()
        # if form.is_valid():
        #     return redirect('f1')
    return render(request,'home.html',{'form':form})
# def index(request):
#     data=student.objects.all()
#     return render(request,'f1.html',{'d':data})
   