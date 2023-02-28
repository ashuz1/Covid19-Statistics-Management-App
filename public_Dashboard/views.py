from django.shortcuts import render
import mysql.connector as sql

def dashaction(request):
    return render(request,'public_dashboard.html')
