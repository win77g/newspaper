from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def category(request,name):
    nama_category = name
    return render(request,'category_page.html',context={'name_category':nama_category})
