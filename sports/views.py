from rest_framework.viewsets import ModelViewSet
import django_filters.rest_framework
from django.db.models import Q
from .serializers import TournamentSerializer, TeamSerializer, GameSerializer
from .models import Game, Team, Tournament

class TournamentViewSet(ModelViewSet):
    queryset = Tournament.objects.filter(Q(status='PLANNED') | Q(status='LIVE'))
    serializer_class = TournamentSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'status']


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
