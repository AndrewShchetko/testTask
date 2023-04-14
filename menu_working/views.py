from django.shortcuts import render
from .models import Menu
from .forms import FindMenuForm


def find_menu(all_menus, menu_name):
    menu: dict = {}
    for menu_ in all_menus:
        if menu_.menu_name == menu_name:
            menu[menu_.name] = menu_
    return menu


def draw_menu(request, menu_slug):
    all_menus = Menu.objects.all()
    menu_object = None
    for obj in all_menus:
        if obj.slug == menu_slug:
            menu_object = obj
            break
    menu_name = ''
    for menu_ in all_menus:
        if menu_.slug == menu_slug:
            menu_name = menu_.menu_name
    prev_context: dict = find_menu(all_menus, menu_name)
    menu: list = []
    name = menu_object.name
    if menu_object:
        depth = prev_context[name].depth
        next_menu_object_order = menu_object.order
        for key, value in prev_context.items():
            if prev_context[key].depth == depth and prev_context[key].order > prev_context[name].order:
                next_menu_object_order = value.order
                break
            else:
                next_menu_object_order = len(prev_context)
        for key, value in prev_context.items():
            condition: bool = (prev_context[key].depth <= menu_object.depth) or \
                            (prev_context[key].depth == depth + 1
                             and
                             menu_object.order < prev_context[key].order < next_menu_object_order)
            if condition:
                menu.append(value)
    else:
        depth = prev_context[menu_object.name].depth
        menu.append(prev_context[menu_object.name])
        for key, value in prev_context:
            if prev_context[key].depth == depth + 1:
                menu.append(value)
    context: dict = {'menu': menu}
    return render(request, 'menu_working/index.html', context=context)


def draw_main_menu(request):
    all_menus = Menu.objects.all()
    menus: list = []
    for menu_ in all_menus:
        if menu_.depth == 0:
            menus.append(menu_)
    context: dict = {'menus': menus}
    return render(request, 'menu_working/base.html', context=context)


def find_menu_and_draw(request):
    if request.method == 'POST':
        form = FindMenuForm(request.POST)
        if form.is_valid():

    else:
        form = FindMenuForm()

    return draw_menu(request, menu_slug)
