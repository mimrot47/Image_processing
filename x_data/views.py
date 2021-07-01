from django.shortcuts import render,redirect
from .models import petaint
from .forms import pataintForm
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
    form=pataintForm()
    if Request.method=='POST':
        username=Request.POST.get('username')
        password=Request.POST.get('password')
        user=authenticate(Request,username=username,password=password)
        if user is not None:
            return redirect('../pateint')
        else:
            pass
    MYDICT={'form':form,'word_data':data,'mhdata':mhdata}
    return render(Request,'./registration/login.html',MYDICT)



@login_required
def patint(Requet):
    return render(Requet,'./pdata/petaint.html')
