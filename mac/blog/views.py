from django.shortcuts import render

from django.http import HttpResponse

from .models import Blogpost
from math import  ceil

# Create your views here.
def index(request):

    mypost=Blogpost.objects.all()

    return render(request,'blog/index.html',{'mypost':mypost})




def blogPost(request,id):
    post=Blogpost.objects.filter(post_id=id)[0]

    print(post)
    return render(request,'blog/blogPost.html',{'post':post})
