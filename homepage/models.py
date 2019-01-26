from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    name = models.CharField(max_length=50,)
    slug = models.SlugField(max_length=50,unique=True)


     # вывод одного поля
    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

def image_folder(instance,filename):
    filename = instance.slug +'.'+filename.split('.')[1]
    return "{0}/{1}".format(instance.slug,filename)

class Posts(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,unique=True)
    # category = models.ForeignKey(Categorys,on_delete=models.PROTECT,default=None, null=True,blank=True)
    category = models.ManyToManyField(Category,blank=True)
    image = models.ImageField(upload_to=image_folder, blank=True, null=True, default=None)
    description = models.TextField(blank=True)
    description_short = models.TextField(blank=True)
    author = models.CharField(max_length=150,default=None)
    date_pub = models.DateTimeField(auto_now_add=True)

     # вывод одного поля
    def __str__(self):
        return " %s" % self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def image_img(self):
        if self.image:
            return  mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
            # return mark_safe(u'<img src="%s" style="width: 45px; height:45px;" />' % self.image.url)
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True


