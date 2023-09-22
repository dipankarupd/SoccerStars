from django.shortcuts import render
from .models import Footballer

# Create your views here.

players = [
    Footballer('Alisson', 'GK', 'Liverpool'),
    Footballer('Destiny Udogie', 'LB', 'Spurs'),
    Footballer('Ruben Dias', 'CB', 'Man City'),
    Footballer('Fabian Schar', 'CB', 'Newcastle'),
    Footballer('Trent', 'RB', 'Liverpool'),
    Footballer('Casemiro', 'CDM', 'Man United'),
    Footballer('Rodri', 'CDM', 'Man City'),
    Footballer('James Maddison', 'CAM', 'Spurs'),
    Footballer('Earling Haaland', 'ST', 'Man City'),
    Footballer('Mitoma', 'LW', 'Brighton'),
    Footballer('Sterling', 'RW', 'Chelsea'),
]


def index(req):
    return render(req, 'index.html', {'players': players})