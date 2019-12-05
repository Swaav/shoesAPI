"""shoes URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from django.conf.urls import url, include
from apishoe import models, views
from rest_framework import routers

admin.site.register(models.Manufacturer)
admin.site.register(models.ShoeType)
admin.site.register(models.ShoeColor)
admin.site.register(models.Shoe)


router = routers.DefaultRouter()
router.register(r'manufacturer', views.Manufacturer_View)
router.register(r'shoetype', views.ShoeType_View)
router.register(r'shoecolor', views.ShoeColor_View)
router.register(r'shoe', views.Shoe_View)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
