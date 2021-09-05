from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from loginPage.utils import get_db_handle, get_collection_handle, validatePassword
import datetime;
  


db_handle, mongo_client = get_db_handle("gymMaster", "localhost", 27017, "", "")
# collection_handle = get_collection_handle(db_handle, "dev")
# collection_handle.find({...})

# collection_handle.update({...})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def loginPage(request):
    print("Login Page Called")
    
    return render(request,"gym_login.html");

def doLogin(request):

    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")

    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if (len(username)!= 0 and len(password)!= 0 ):

        if (validatePassword(db_handle,username,password)):
            return  redirect('addUser')
        else: #Add failed login attempts into Database
            login_collection = get_collection_handle(db_handle, "login_log")
            sso = login_collection.insert({"case":"login performed","username":username, "password":password,"time_stamp":datetime.datetime.now()})
            messages.error(request,"Invalid Credentials")
            return redirect('login')
    else:
        messages.error(request,"Username or Password cannot be empty")
        return redirect('login')

    
def addUser(request):
    return render(request,"gym_addUser.html")

