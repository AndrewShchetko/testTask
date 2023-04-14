from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name='menu item name')
    slug = models.SlugField(max_length=25, unique=True, db_index=True, verbose_name='slug')
    menu_name = models.CharField(max_length=25, verbose_name='Name of item patent menu')
    order = models.IntegerField(unique=True, default=0, verbose_name='Database order')
    depth = models.IntegerField(default=0, verbose_name='Item depth')

    def get_absolute_url(self):
        return reverse('draw_menu', kwargs={'menu_slug': self.slug})

    class Meta:
        ordering = ['order']
