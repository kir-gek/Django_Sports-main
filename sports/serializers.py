from rest_framework.serializers import ModelSerializer
from .models import Game, Team, Tournament


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class TournamentSerializer(ModelSerializer):
    class Meta:
        model = Tournament
        fields = '__all__'
