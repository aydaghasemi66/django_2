from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

    
class Client(models.Model):
    info = models.ForeignKey(User , on_delete=models.CASCADE)
    job = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='client')
    

    def __str__(self):
        return self.info.username
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


    

class Gallery(models.Model):
    
    image = models.ImageField(upload_to='photo')
    client_company=models.CharField(max_length=100)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    project_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
    
    def capt(self):
        return self.title.capitalize()







    
    







 