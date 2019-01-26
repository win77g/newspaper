from .models import Category

def news_info(request):
    category = Category.objects.all()


    return locals()
