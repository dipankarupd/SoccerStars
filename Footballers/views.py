from django.shortcuts import render, redirect
from .models import Footballer
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def index(req):
    players = Footballer.objects.all()
    return render(req, 'index.html', {'players': players})

def register(req):

    if req.method == 'POST':
        username = req.POST['Username']
        email = req.POST['Email']
        password = req.POST['Password']
        password2 = req.POST['Password2']


        if password == password2 :
            if User.objects.filter(email = email).exists():
                messages.info(req, 'Email already in use')
                return redirect('register')

            elif User.objects.filter(username = username).exists():
                messages.info(req, 'Username already in use')
                return redirect('register')

            else:
                user = User.objects.create_user(username = username, email = email, password = password)
                user.save()
                return redirect('login')

        else:
            messages.info(req, 'Password do not match')
            return redirect('register')
    else:
        return render(req, 'register.html')

    
def login(req):

    if req.method == 'POST':

        username = req.POST['Username']
        password = req.POST['Password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(req,user)
            return redirect('/')
        else:
            messages.info(req, 'Invalid credentials')
            return redirect('login')
    else:
        return render(req, 'login.html')
            
    