from django.urls import path
from .views import *

app_name = 'gallery'

urlpatterns = [
    path('gallery_detail/<int:id>/', gallery_detail, name='gallery-detail'),
    path("category/<str:cat>",gallery ,name ="gallery_cat"),
]