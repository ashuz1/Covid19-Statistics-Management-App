from django.shortcuts import render , redirect
import mysql.connector as sql
from genraldashboard.views import categorylisting
from aprove_page.views import aproveaction

un=''
upwd =''


# Create your views here.
def loginaction(request):
    global un,upwd
    if request.method == "POST":
        m=sql.connect(host="localhost",user = "root",passwd ="88monu58",database = "covid19db")
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key =="uname":
                un = value
            if key == "psw":
                upwd = value
        
        c="select user_role from user_table where user_name ='{}' and user_password ='{}'".format(un,upwd)
        cursor.execute(c)
        t =tuple(cursor.fetchall())
        print(t[0])

        if t==():
            return render(request,'error.html')
        elif t[0] == ('admin',):
            return redirect(aproveaction)
        elif t[0] == ('user',):
            return redirect(categorylisting)
        else:
            return render(request,'error.html')
    return render(request,'login_page.html')
    