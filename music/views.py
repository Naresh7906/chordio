from logging import error
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .DBedit import DBconn
from django.contrib.sessions.models import Session

class error:
    def __init__(self):
        self.reg_error = False
        self.log_error = False


err = error()



dbobj = DBconn()

def index(request):
    err.log_error = False
    err.reg_error = False
    result = dbobj.show_songs_web()
    return render(request, "index.html", {"songs": result})

def Album(request):
    result = dbobj.show_album_web()
    return render(request, "album.html",{"album":result})


def profile(request): 
    if request.session.has_key('email'):
        email=request.session['email']
        data = dbobj.user_data(email)
        return render(request, "profile.html", {"name": request.session['email'],"result":data})  
    else:
        return render(request,"login.html")      

def search(request):
    ser = str(request.POST['ser'])
    result = dbobj.find_songs_web(ser)
    return render(request, "index.html", {"songs": result})

def login(request):
    if request.session.has_key('email'):
        return redirect('index')
    else:
        if request.POST:    
            request.session['email'] = request.POST['email']
            return redirect('index')
        return render(request, "login.html",{"error": err.log_error})

def VerifyUser(request):
    email = str(request.POST['email'])
    password = str(request.POST['password'])
    verify = dbobj.get_user(password,email)
    if verify == True :
        err.log_error = False
        request.session['email'] = email
        return redirect('index')
    err.log_error=True
    return redirect('login')

def SaveData(request):
    f_name = str(request.POST["f_name"])
    l_name = str(request.POST["l_name"])
    email = str(request.POST["email"])
    password = str(request.POST["password"])
    if dbobj.user_exist(email):
        err.reg_error = True
        return redirect('register')
    dbobj.add_user(f_name,l_name,email,password)
    err.reg_error=False
    return redirect('index')



def EditData():
    email = request.session['email']
    result = dbobj.user_data(email)
    if request.POST['inputFname']!='':
        uf_name = str(request.POST['inputFname'])
    else:
        uf_name=result[0][1]

    if request.POST['inputLname']!='':
        ul_name = str(request.POST['inputLname'])
    else:
        ul_name=result[0][2]

    if request.POST['inputPassword']!='':
        upassword = str(request.POST['inputPassword'])
    else:
        upassword=result[0][3]

    dbobj.update_user(uf_name,ul_name,upassword,email)
    return redirect('index')
    

def register(request):
    if request.session.has_key('email'):
        err.reg_error = False
        return redirect('index')

    return render(request, "register.html",{"error": err.reg_error})

def delete(request):
    if request.POST:
        mail=request.session['email']
        dbobj.delete_user(mail)
        request.session.flush()

        return redirect('login')

def about(request):
    if request.session.has_key('email'):
        return render(request, "about.html", {"name": request.session['email']})
    else:
        return render(request, "about.html")

def logout(request):
    request.session.flush()
    return redirect('index')

def player(request):
    return render(request, "music_player.html")

def upload(request):
    return render(request, "upload.html")