from django.shortcuts import render
from django.http import HttpResponse
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

    if (username is not None and password is not None):
        
        #Add failed login attempts into Database

        if (validatePassword(db_handle,username,password)):
            return HttpResponse("Login Success")
        else:
            login_collection = get_collection_handle(db_handle, "login_log")
            sso = login_collection.insert({"case":"login performed","username":username, "password":password,"time_stamp":datetime.datetime.now()})
            return HttpResponse("Login Failed")
    
    

