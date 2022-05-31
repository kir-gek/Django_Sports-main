from django.contrib import admin
from .models import Game, Team, Tournament

admin.site.register(Game)
admin.site.register(Team)
admin.site.register(Tournament)