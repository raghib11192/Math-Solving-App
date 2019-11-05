"""raghibmainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from testApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('class9/', views.class9),
    path('facts9/',views.fact9,name='raj'),
    path('quadrants9/', views.quadrant9,name='raj1'),
    path('areaOfTraingles9/', views.areaOfTraingle9,name='raj2'),
    path('areaOfTrainglesBaseHeight9/', views.areaOfTraingleBaseHeight9,name='raj3'),
    path('areaOfQuadrilateral/', views.areaOfQuadrilateral,name='raj4'),
    path('areaOfParallelogram/', views.areaOfParallelogram,name='raj5'),
    path('areaOfRohumbus/', views.areaOfRohumbus,name='raj6'),
    path('volumeOfCuboid/', views.volumeOfCuboid,name='raj7'),
    path('volumeOfCube/', views.volumeOfCube,name='raj8'),
    path('volumeOfCylender/', views.volumeOfCylender,name='raj9'),
    path('volumeOfCone/', views.volumeOfCone,name='raj10'),
    path('volumeOfSphere/', views.volumeOfSphere,name='raj11'),

]
