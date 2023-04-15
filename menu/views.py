from django.shortcuts import render
from .models import Menu, MenuItems

def menu_page(request, active=None):
    context = {"active": active}
    return render(request, 'base.html', context=context )


#def menu(request):
#    items = MenuItems.objects.filter(menu=1).select_related('parent').values("name", "menu")
#    print(items)
#    context = {"items": items}
#    return render(request, 'menu.html', context=context )
    
# Create your views here.
