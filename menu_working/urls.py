from django.urls import path
from . import views


urlpatterns = [
    path('', views.draw_main_menu, name='main_menu'),
    path('menu/<slug:menu_slug>', views.draw_menu, name='draw_menu'),
]
