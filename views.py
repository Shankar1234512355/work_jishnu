from django.shortcuts import render
from app1.models import *
from django.http import HttpResponseRedirect
import pyautogui as pya
from django.core.files.storage import FileSystemStorage

# Create your views here.
def login(request):
    if request.POST.get('sub'):
        u=request.POST.get('username')
        p=request.POST.get('password')
        try:
            data=login_tb.objects.get(username=u,password=p)
            ut=data.utype

            request.session["user"]=data.username  #database username
        
            if ut=="admin":
                return HttpResponseRedirect('admin')
            elif ut=="volunteer":
                return HttpResponseRedirect('volunteer')
            elif ut=="police":
                return HttpResponseRedirect('police')
            elif ut=="member":
                return HttpResponseRedirect('member')    
        except:
            pya.alert(text="username or password are incorrect",title="failed")        
    return render(request,"login.html",{})

def signup(request):
    if request.POST.get('add'):
        n=request.POST.get('name')
        ph=request.POST.get('contact')
        e=request.POST.get('email')
        p=request.POST.get('pwd')
        a=request.POST.get('address')
        u=request.POST.get('username')
        d=request.POST.get('district')
        s=request.POST.get('state')
        if login_tb.objects.filter(username=u).exists():
            pya.alert(text="already exist",title="exist")
            return HttpResponseRedirect("signup")
        else:    
            data=member_tb(name=n,Phone=ph,email=e,password=p,address=a,District=d,State=s,username=u)
            data.save()
            
            if data is not None:
                data2=login_tb(username=u,password=p,utype='member')
                data2.save()
                # pya.alert(text="New customer added",title="Add new data")
                return HttpResponseRedirect("./")
    return render(request,"signup.html",{})    

def admin(request):
    if request.POST.get('vsub'):
        n=request.POST.get('vname')
        a=request.POST.get('age')
        ph=request.POST.get('phone')
        s=request.POST.get('state')
        d=request.POST.get('district')
        u=request.POST.get('username')
        p=request.POST.get('password')
        data=volunteer_tb(name=n,age=a,Phone=ph,State=s,District=d,username=u,password=p)
        data.save()
        
        if data is not None:
            data2=login_tb(username=u,password=p,utype='volunteer')
            data2.save()
            pya.alert(text="New volunteer added",title="Add new data")
            return HttpResponseRedirect("admin")

    if request.POST.get('psub'):
        n=request.POST.get('vname')
        a=request.POST.get('age')
        ph=request.POST.get('phone')
        s=request.POST.get('state')
        d=request.POST.get('district')
        u=request.POST.get('username')
        p=request.POST.get('password')
        data=police_tb(name=n,age=a,Phone=ph,State=s,District=d,username=u,password=p)
        data.save()
        
        if data is not None:
            data2=login_tb(username=u,password=p,utype='police')
            data2.save()
            pya.alert(text="New police added",title="Add new data")
            return HttpResponseRedirect("admin")        
    return render(request,"admin.html",{})  

def volunteer(request):
    v=request.session['user']
    if request.POST.get('sub'):
        l=request.POST.get('location')
        p=request.POST.get('police')
        i=request.FILES['img']
        fs=FileSystemStorage()
        fs.save("app1/static/images/"+i.name,i)

        data1=message_tb(location=l,police=p,image=i.name)
        data1.save()

        if data1 is not None:
            pya.alert(text="new penalty added",title="Penalty added")
            return HttpResponseRedirect("volunteer")
    data=police_tb.objects.all()
    return render(request,"volunteer.html",{'data':data,'v':v})  

def police(request):
    p=request.session['user']
    if request.POST.get('add'):
        n=request.POST.get('name')
        a=request.POST.get('address')
        d=request.POST.get('district')
        s=request.POST.get('state')
        u=request.POST.get('username')
        i=request.FILES['img']
        fs=FileSystemStorage()
        fs.save("app1/static/images/"+i.name,i)

        data=penalty_tb(name=n,address=a,District=d,State=s,username=u,image=i)
        data.save()
    return render(request,"police.html",{'p':p})    

def message(request):
    data=message_tb.objects.all()
    return render(request,"message.html",{'data':data})

def member(request):
    m=request.session['user']
    data=campaign_tb.objects.all()
    return render(request,"member.html",{'m':m,'data':data}) 

def penalty(request):
    m=request.session['user']
    a=member_tb.objects.values_list('address').filter(username=m)
    b=penalty_tb.objects.filter(address__in=a)
    c=rehab_tb.objects.filter(address__in=a)
    print(c)
    # d=penalty_tb.objects.filter(username=m).values_list('address','image','penalty')
    return render(request,"penalty.html",{'b':b,'c':c}) 

def campaigns(request):
    if request.POST.get('sub'):
        l=request.POST.get('location')
        cg=request.POST.get('guest')
        d=request.POST.get('description')
        i=request.FILES['img']
        fs=FileSystemStorage()
        fs.save("app1/static/images/"+i.name,i)

        data=campaign_tb(location=l,chief_guest=cg,Description=d,image=i)
        data.save()
    return render(request,"vcampaigns.html",{})

def info(request):
    data=volunteer_tb.objects.all()
    data1=police_tb.objects.all()
    data2=member_tb.objects.all()
    return render(request,"info.html",{'data':data,'data1':data1,'data2':data2})   

def post(request):
    data=campaign_tb.objects.all()
    return render(request,"post.html",{'data':data})    

def rehab(request):
    p=request.session['user']
    if request.POST.get('add'):
        u=request.POST.get('username')
        lo=request.POST.get('location')
        sd=request.POST.get('sdate')
        ed=request.POST.get('edate')
        data1=rehab_tb(member_username=u,rehab_location=lo,start_date=sd,end_date=ed,police=p)
        data1.save()
        
    return render(request,"rehab.html",{})

def demo(request):
    return render(request,"demo.html",{})  


    
    