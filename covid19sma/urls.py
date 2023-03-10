"""covid19sma URL Configuration

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
from django.urls import path , include
from login_page.views import loginaction
from adddetails.views import addaction
from genraldashboard.views import categorylisting 
from aprove_page.views import aproveaction , setaprove

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_page/',loginaction),
    path('',include('public_Dashboard.urls')),
    path('add_details/',addaction),
    path('genral_dashboard/',categorylisting),
    path('aprove_page/',aproveaction),
    path('aprove_page/<int:id>',setaprove,name="setaprove"),
]
