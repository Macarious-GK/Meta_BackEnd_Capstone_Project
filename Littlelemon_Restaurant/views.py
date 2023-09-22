from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse

from .serializer import *
from .models import *

from rest_framework import status, viewsets, generics
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.contrib.auth.models import User,Group
from django.core.paginator import EmptyPage, Paginator
from django.views.generic.base import TemplateView 

# Create your views here.
def H(request):
    return HttpResponse('Hello world')

def index(request):
    return render(request, 'index.html', {})


@api_view(['GET','POST'])
def MenuItemView(request):
    if request.method == 'GET':
        menuitems = Menu.objects.all()
        menuserializer = menuSerializer(menuitems, many = True)
        return Response({'message':menuserializer.data},200)
    elif request.method == 'POST':
        menuserializer = menuSerializer(data=request.data)
        if menuserializer.is_valid():
            menuserializer.save()
            return Response({'message':menuserializer.data},201)
        else:
            return Response({'message':menuserializer.errors},400)
    else:
        return Response({'message':'Bad Request'},400)
    


class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    def delete(self, request, *args, **kwargs):
        menudeleted = self.get_object()
        menudeleted.delete()
        return Response({'message': 'Menu item deleted successfully'}, 200)
    def update(self, request, *args, **kwargs):
        menuupdated = self.get_object()
        menuitemserializer = menuSerializer(menuupdated,data = request.data)
        if menuitemserializer.is_valid():
            menuitemserializer.save()
            return Response(menuitemserializer.data, status=200)
        return Response(menuitemserializer.errors, status=400)
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 
