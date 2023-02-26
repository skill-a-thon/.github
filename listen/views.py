from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .decorators import unAuthenticated_user
from django.contrib.auth.decorators import login_required
from .student_sight import monitor
import json
import threading

@unAuthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            usrObj = User(username=username)
            fullname = usrObj.first_name + usrObj.last_name
            email = usrObj.email
            user_data = {
                'fullname': fullname,
                'email': email,
                'username': username
            }
            f = open('usr_data.json','w')
            json_dump = json.dump(user_data,f)
            '''with open('usr_data.json', 'w') as out:
                out.write(json_dump)'''
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'listen/index.html')
    return render(request, 'listen/index.html')

@login_required(login_url='login')
def home(request):
    thread = threading.Thread(target=monitor.start, name='MonitorThread')
    thread.start()
    return render(request, 'listen/home.html')

@login_required(login_url='login')
def logout_func(request):
    logout(request)
    return redirect('login')