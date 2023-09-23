from django.shortcuts import render
from .models import Footballer

# Create your views here.

def index(req):

    players = Footballer.objects.all()
    return render(req, 'index.html', {'players': players})