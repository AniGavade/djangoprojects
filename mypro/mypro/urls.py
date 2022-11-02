"""mypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from newapp import views
from meranayaapp import views as v1
from android import views as v2


router=DefaultRouter()
router.register('userapi',views.newclass,basename="newclass")
router.register('singerapi',v1.Singerviewset,basename="singer")
router.register('songapi',v1.Songviewset,basename="song")
router.register("appapi",v2.BwksStuViewset,basename="appapi")

urlpatterns = [
    path('myapp/',include('myapp.urls')),
    path('newapp/',include('newapp.urls')),
    path('admin/', admin.site.urls),
    path('currapp',include("currapp.urls")),
    path("",include(router.urls)),
    path("meranayapp",include(router.urls)),
    path("android",include("android.api.urls")),
    path("appapi",include(router.urls))
]
 
