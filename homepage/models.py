from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,)
    slug = models.SlugField(max_length=50,unique=True)


     # вывод одного поля
    def __str__(self):
        return " %s" % self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
