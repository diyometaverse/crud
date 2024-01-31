from django.shortcuts import render, redirect
from .models import Member
# Create your views here.

def index(request):
    mem=Member.objects.all()
    return render(request, 'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrecord(request):
    x=request.POST['fname']
    y=request.POST['sec']
    z=request.POST['yr']
    mem=Member(fullname=x,section=y,year=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Member.objects.get(id=id)
    return render(request, 'update.html', {'mem':mem})

def updaterecord(request,id):
    x=request.POST['fname']
    y=request.POST['sec']
    z=request.POST['yr']
    mem=Member.objects.get(id=id)
    mem.fullname=x
    mem.section=y
    mem.year=z
    mem.save()
    return redirect("/")