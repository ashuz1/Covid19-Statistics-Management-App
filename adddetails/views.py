from django.shortcuts import render , redirect
import mysql.connector as sql
from genraldashboard.views import categorylisting

ustate=''
totalc =''
recoverdc =''
activec = ''
tdeths = ''
tvaccinated = ''
tdate =''



# Create your views here.
def addaction(request):
    global ustate, totalc,recoverdc,activec ,tdeths ,tvaccinated,tdate
    if request.method == "POST":
        m=sql.connect(host="localhost",user = "root",passwd ="88monu58",database = "covid19db")
        cursor = m.cursor()

        d=request.POST
        for key,value in d.items():
            if key=="state":
                ustate=value
            if key=="total_cases":
                totalc=value
            if key=="recoverd_cases":
                recoverdc=value
            if key=="active_cases":
                activec=value
            if key=="deth_cases":
                tdeths=value
            if key=="vaccinated":
                tvaccinated=value
            if key=="date_created":
                tdate=value
            
        
        c="insert into covid_today(user_state,total_cases,recoverd_cases,active_cases,deth_cases,vaccinated,date_created) Values('{}','{}','{}','{}','{}','{}','{}')".format(ustate,totalc,recoverdc,activec,tdeths,tvaccinated,tdate)
        cursor.execute(c)
        m.commit()
        #return redirect(categorylisting)
    #return redirect(categorylisting)
    return render(request,'add_details.html')
    

# Create your views here.
