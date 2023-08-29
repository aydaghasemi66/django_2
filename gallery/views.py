from django.shortcuts import render, get_object_or_404
from .models import *

def gallery_detail(request, id):
    galleries = get_object_or_404(Gallery, id=id)
    client = Client.objects.get(id=id)
    

    context = {
        'galleries': galleries,
        'client' : client,
        
    }
    return render(request, 'gallery/gallery-single.html', context=context)

def gallery(request, cat=None ):
    category = Category.objects.all()
    gallery= Gallery.objects.all()

    
    context = {
        'gallery': gallery,
        'category': category,
    }
    return render(request, 'gallery/gallery.html', context=context)


  