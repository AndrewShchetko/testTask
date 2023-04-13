from django.shortcuts import render
from .models import Menu


def find_menu(all_menus, menu_slug):
    menu: dict = {}
    menu_name = ''
    for menu_ in all_menus:
        if menu_.slug == menu_slug:
            menu_name = menu_.menu_name
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
    prev_context: dict = find_menu(all_menus, menu_slug)
    menu: list = []
    name = menu_object.name
    if menu_object:
        depth = prev_context[name].depth
        next_menu_object = menu_object
        for key, value in prev_context.items():
            if prev_context[key].depth == depth and prev_context[key].order > prev_context[name].order:
                next_menu_object = value
                print(next_menu_object)
                break
        for key, value in prev_context.items():
            condition: bool = (prev_context[key].depth <= menu_object.depth) or \
                            (prev_context[key].depth == depth + 1
                             and
                             menu_object.order < prev_context[key].order < next_menu_object.order)
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
