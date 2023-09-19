from django.urls import path
from .views import *
from . import views
# from schema_graph.views import Schema
urlpatterns = [
    path('1/',H,name = 'fifa'),
    path('', views.index, name='home'),
    

]



