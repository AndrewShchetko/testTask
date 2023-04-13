from django.db import models
from django.urls import reverse


class Menu(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=25, unique=True, db_index=True)
    menu_name = models.CharField(max_length=25)
    order = models.IntegerField(unique=True, default=0)
    depth = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('draw_menu', kwargs={'menu_slug': self.slug})

    class Meta:
        ordering = ['order']
