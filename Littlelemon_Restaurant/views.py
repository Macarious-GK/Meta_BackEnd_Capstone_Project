from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse

from .serializer import *
from .models import *

from rest_framework import status, viewsets, generics
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.contrib.auth.models import User,Group
from django.core.paginator import EmptyPage, Paginator
from django.views.generic.base import TemplateView 

# Create your views here.
def H(request):
    return HttpResponse('Hello world')