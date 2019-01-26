from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin (admin.ModelAdmin):
    list_display = ["name"]


class Meta:
    model = Category
# Register your models here.
admin.site.register(Category,CategoryAdmin)
