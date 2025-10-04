from rest_framework import viewsets
from django.shortcuts import render
from .models import Player, Club, League
from .serializers import PlayerSerializer, ClubSerializer, LeagueSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

def index(request):
    return render(request, 'core/index.html')