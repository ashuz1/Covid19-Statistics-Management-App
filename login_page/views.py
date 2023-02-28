from django.shortcuts import render
import mysql.connector as sql

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
            return render(request,'aprove.html')
        elif t[0] == ('user',):
            return render(request,'genral_dashboard.html')
        else:
            return render(request,'error.html')
    return render(request,'login_page.html')
    