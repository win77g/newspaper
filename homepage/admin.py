from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin (admin.ModelAdmin):
    list_display = ["name"]


class Meta:
    model = Category
# Register your models here.
admin.site.register(Category,CategoryAdmin)

class PostsAdmin (admin.ModelAdmin):
    list_display = ['title','show_category','image_img','author','date_pub']
    def show_category(self, obj):
        return "\n".join([a.slug for a in obj.category.all()])
    #  вывод всех полей в админку
    #   list_display = [field.name for field in Posts._meta.fields]
    #  фильтр  натройка
    list_filter = ['title']
    #   поиск
    search_fields = ['id','title','date_pub']
    readonly_fields = ['image_img',]
    # for Many to Many
    # def get_categorys(self, obj):
    #     return "\n".join([p.category for p in obj.category.all()])

class Meta:
    model = Posts
# Register your models here.
admin.site.register(Posts,PostsAdmin)
