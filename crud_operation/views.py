from django.shortcuts import render,redirect,HttpResponseRedirect
from crud_operation.forms import StudetnRegistration
from.models import UserStudent
# Create your views here.
# this fucntion will add new itms and show All items
def add_show(request):
    if request.method=='POST': 
        fm=StudetnRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=UserStudent(name=nm,email=em,password=pw)
            reg.save()
        return redirect('addandshow')

    else:
        fm=StudetnRegistration()
    students = UserStudent.objects.all()
    return render(request,"crud_operation/addandshow.html",{'form':fm,'student':students})
# this function Will Update/Edit

def update_data(request,id):
    if request.method=='POST':
        pi=UserStudent.objects.get(pk=id)
        fm=StudetnRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=UserStudent.objects.get(pk=id)
        fm=StudetnRegistration(instance=pi)
    return render(request,"crud_operation/update.html",{'form':fm})
# this function will delete
def delete_data(request,id):
    if request.method=='POST':
        pi=UserStudent.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')