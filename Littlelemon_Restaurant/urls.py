from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)
urlpatterns = [
    path('1/',H,name = 'f'),
    path('', views.index, name='home'),
    path('menu-items/',MenuItemView,name='MenuItems'),
    path('menu-items/<int:pk>/',SingleMenuItemView.as_view(),name='MenuItems'),


]
urlpatterns +=router.urls



