from django.contrib import admin
from django.urls import path
from public_Dashboard.views import dashaction

urlpatterns = [
    path('',dashaction),
]