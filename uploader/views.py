from django.shortcuts import render,redirect
from uploader import models
from .models import Imager
from email.mime import image
import os

# Create your views here.
def index(request):
    if request.method=="POST":
        im=Imager()
        im.title=request.POST.get('title')
        if len(request.FILES)!=0:
            im.image=request.FILES['image']
        im.save()
        return redirect('/')
    else:
        data=Imager.objects.all()
    return render(request,'index.html',{'data':data})

def edit(request,id):
    im=Imager.objects.get(id=id)
    if request.method=='POST':
        im.title=request.POST.get('title')
        if len(request.FILES)!=0:
            if len(im.image)>0:
                os.remove(im.image.path)
            im.image=request.FILES['image']
        im.save()
        return redirect('/')

    context={
        'im':im
    }
    return render(request, 'edit.html',context)

def delete(request,id):
    des=Imager.objects.get(id=id)
    des.delete()
    return redirect('/')
    context={
        'im':im
    }
    return render(request,'index.html',context)
