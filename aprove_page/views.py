from django.shortcuts import render , redirect
import mysql.connector as sql




# Create your views here.
m=sql.connect(host="localhost",user = "root",passwd ="88monu58",database = "covid19db")
cursor = m.cursor()

def aproveaction(request):
    cursor.execute("SELECT * FROM covid_today")
    data = cursor.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'aprove.html', {'categories': data})

def setaprove(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cursor.execute("insert into covid_stastics(user_state,total_cases,recoverd_cases,active_cases,deth_cases,vaccinated,date_updated) select user_state,total_cases,recoverd_cases,active_cases,deth_cases,vaccinated,date_created from covid_today where user_id = {}".format(id))
    m.commit()
    cursor.execute("delete from covid_today where user_id = {}".format(id))
    m.commit()
    return redirect(aproveaction)