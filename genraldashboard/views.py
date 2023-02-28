from django.shortcuts import render,redirect
 
from django.http import HttpResponse
# Create your views here.
import mysql.connector as sql

# Create your views here.
m=sql.connect(host="localhost",user = "root",passwd ="88monu58",database = "covid19db")
cursor = m.cursor()
