from django.db import models

# Create your models here.

class Footballer:
    Name: str
    Position: str
    Team: str

    def __init__(self, Name, Position, Team):
        self.Name = Name
        self.Position = Position
        self.Team = Team

