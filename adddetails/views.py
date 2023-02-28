from django.shortcuts import render
import mysql.connector as sql

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
            
        
        c="insert into covid_today Values('{}','{}','{}','{}','{}','{}','{}')".format(ustate,totalc,recoverdc,activec,tdeths,tvaccinated,tdate)
        cursor.execute(c)
        m.commit()
    return render(request,'add_details.html')
    

# Create your views here.
