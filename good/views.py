from django.shortcuts import render
from .models import Blog
# Create your views here.
dd=[]

def home(request):
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs,'dd':dd})
def result(request):
    ang1=request.GET['hoho']
    blogs=Blog.objects
    a=1
    for blog in blogs.all():
        if ang1==blog.body:
            a=2
            dd.append(blog.number)
    return render(request,'result.html',{'ang1':a,'dd':dd})