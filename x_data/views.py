from django.shortcuts import render,redirect
from .models import petaint
from .forms import pataintForm,SignUpForm
import requests
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(Request):
    url='https://api.covid19api.com/summary'
    mhurl='https://api.covid19india.org/data.json'
    mhr=requests.get(mhurl)
    r=requests.get(url)
    data=r.json()
    mhdata=mhr.json()
    covid=petaint.objects.filter(p_covid='Positive').count()
    form=pataintForm()
    if Request.method=='POST':
        username=Request.POST.get('username')
        password=Request.POST.get('password')
        user=authenticate(Request,username=username,password=password)
        if user is not None:
            return redirect('../pateint')
        else:
            msg={'msg':"Username or Password wrong..."}
            MYDICT={'form':form,'word_data':data,'mhdata':mhdata,'covid':covid,'msg':msg}
            return render(Request,'./registration/login.html',MYDICT)
    MYDICT={'form':form,'word_data':data,'mhdata':mhdata,'covid':covid}
    return render(Request,'./registration/login.html',MYDICT)



@login_required
def patint(Requet):
    pataints_list=petaint.objects.all()
    MYDICT={'DATA':pataints_list}
    return render(Requet,'./pdata/petaint.html',MYDICT)


def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return redirect('../')
    return render(request,'./registration/signup.html',{'form':form})

@login_required   
def info(Request,id):
    pataints_list=petaint.objects.get(id=id)
    MYDIC_INFO={'INFO':pataints_list}
    return render(Request,'./pdata/info.html',MYDIC_INFO)

@login_required 
def insert(Request):
    form=pataintForm()
    FORMDICT={'FORM':form}
    if Request.method=='POST':
        form=pataintForm(Request.POST,Request.FILES)
        if form.is_valid():
            form.save()
            return redirect('../pateint')
        else:
            print("Data not Validated")
    return render(Request,'./pdata/insert.html',FORMDICT)
