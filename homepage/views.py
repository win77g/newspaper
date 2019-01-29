from django.shortcuts import render
from .models import Category,Posts

# Create your views here.

def index(request):
    post = Posts.objects.all()

    return render(request,'index.html', context={'post':post})

def category(request,slug):
    name_category = slug
    categ = Category.objects.get(slug__iexact = slug)
    # posts = Posts.objects.filter(category = name_category)

    return render(request,'category_page.html',context={'categ':categ,'name_category':name_category})

def post(request,id):
    post = Posts.objects.get(id = id)
    post.views += int(1)
    post.save()
    print(post.category)

    return render(request,'post_page.html',context={'post':post},)

def slug(request):
    data = request.POST
    slug = data.get('slug')
    categ = Category.objects.get(slug__iexact = slug)
    print(categ)
    return render(request, 'list_news.html', context={'categ':categ})
