from django.urls import path
from menu import views



urlpatterns = [
    path('menu/', views.menu_page, name="basic_page"),
    path('menu/<str:active>', views.menu_page, name="active_page"),
#    path('', views.menu, name="menu" )
]
