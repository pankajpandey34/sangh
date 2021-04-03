"""sangh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from core import views


urlpatterns = [
    path('', views.home, name="home"),  
    path('signup/',views.signup, name="signup"), 
    path('user_login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.profile, name="profile"),

    path('prapatra/', views.prapatra, name="prapatra"),
    path('rajpatra/', views.rajpatra, name="rajpatra"),
    path('5680/', views.niyu, name="5680"),

    path('rankfg/',views.rankfg,name="rankfg"),
    path('rankforester/', views.rankforester, name="rankforester"),
    path('rankaro/', views.rankaro, name="rankaro"),

    path('undercons/', views.undercons, name="undercons"),

    path('calcform/', views.calcform, name="calcform"),
    path('calcform/calcu/', views.calcu, name="calcu"),

    path('fanc/', views.fancing, name="fanc"),
    path('fanc/fancingout/',views.fancingout, name="fancingout"),

    path('gurthwise/', views.gurthwise,name="gurthwise"),

    path('uploadpdf/',views.fileupload.as_view(), name="uploadpdf"),
    path('uploadimage/',views.imageupload, name="uploadimage"),

    path('dfoletter/',views.dfoletter, name="dfoletter"),
    path('ccfletter/',views.ccfletter, name='ccfletter'),
    path('pccfletter',views.pccfletter, name='pccfletter'),
    path('hardasanghletter',views.hardasanghletter, name="hardasanghletter"),
    path('bhopalsanghletter',views.bhopalsanghletter, name="bhopalsanghletter"),
]

