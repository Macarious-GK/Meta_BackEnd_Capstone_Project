"""
URL configuration for Capstone_09_17_2023 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from Littlelemon_Restaurant import views
from django.urls import path, include


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('djoser.urls')),
    path('auth-token/',include('djoser.urls.authtoken')),
    path('',include('Littlelemon_Restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
