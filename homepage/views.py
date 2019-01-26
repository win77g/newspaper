from django.shortcuts import render
from .models import Category,Posts

# Create your views here.

def index(request):
    return render(request,'index.html')

def category(request,slug):
    name_category = slug
    categ = Category.objects.get(slug__iexact = slug)
    # posts = Posts.objects.filter(category = name_category)

    return render(request,'category_page.html',context={'categ':categ,'name_category':name_category})
