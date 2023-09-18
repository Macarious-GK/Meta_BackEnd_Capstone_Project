from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('1/',H,name = 'fifa'),
    path('', views.index, name='home')

]



