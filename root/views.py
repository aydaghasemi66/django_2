from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from gallery.models import *
from .models import *
from django.contrib import messages
from .forms import ContactUsForm
# Create your views here.
def home(request):
    gallery = Gallery.objects.all()
    category= Category.objects.all()
    context = {
        'gallery':gallery,
        'category' : category
    }
    return render(request,"root/index.html",context=context)
def about (request):
    clients= Client.objects.all()
    category= Category.objects.all()
    context = {
        'category' : category,
        'clients': clients
    }
    return render(request,"root/about.html",context=context)

def gallery_detail(request):
    category= Category.objects.all()
    context = {
        'category' : category
    }
    return render(request,'gallery/gallery-single.html',context=context)
def services(request):
    clients= Client.objects.all()
    category= Category.objects.all()
    services = Services.objects.filter(status=True)
    prices=Prices.objects.all()
    context = {
        'category' : category,
        'clients': clients
        ,'services': services
        ,'prices': prices
    }
    return render(request,'root/services.html',context=context)


def contact(request):
    if request.method == 'POST' :
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.add_message(request,messages.SUCCESS,'we received your message and call with you as soon')
            return redirect('root:contact')   
        else :
            messages.add_message(request,messages.ERROR,'Invalid data')
            return redirect('root:contact')
    else:
        category = Category.objects.all()
        context = {
            'category':category,
        }
        return render(request,"root/contact.html",context=context)

def gallery(request,cat=None):
    category= Category.objects.all()
    galleries = Gallery.objects.filter(category__name=cat)
    gallery = Gallery.objects.all()
    context = {
        'gallery' : gallery,
        'category' : category,
        'galleries' : galleries
    }
    return render(request,'gallery/gallery.html',context=context)


        
    
