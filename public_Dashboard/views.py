from django.shortcuts import render
import mysql.connector as sql

from django.shortcuts import render,redirect
 
from django.http import HttpResponse
# Create your views here.
import mysql.connector as sql

# Create your views here.
m=sql.connect(host="localhost",user = "root",passwd ="88monu58",database = "covid19db")
cursor = m.cursor()

def dashaction(request):
    cursor.execute("SELECT * FROM covid_stastics")
    data = cursor.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'public_dashboard.html', {'categories': data})

