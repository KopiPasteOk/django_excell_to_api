from django.urls import path
from .views import *

app_name = "frontend"
urlpatterns = [
    path('', index, name='index'),
    path('contact-us/', contactus, name='contactus'),
    path("blog/<str:slug>", blogdetail, name="blog-detail"),
]
