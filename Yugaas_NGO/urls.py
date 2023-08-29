"""Yugaas_NGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home),
    path('',views.base),
    path('base',views.base),
    path('aboutus',views.aboutus),
    path('services',views.our_services),
    path('card',views.card),
    path('contactus',views.contactus),
    path('faq',views.faq),
    path('aboutus1',views.aboutus1),
    path('aboutus2',views.aboutus2),
<<<<<<< HEAD
    path('login',views.login),

=======
>>>>>>> 85e5e84fecb76bf1f25d14fc8cdc2447d8f4bad8
    #path('<int:id>/',views.detail)

]
