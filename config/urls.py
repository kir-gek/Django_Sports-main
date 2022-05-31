from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from sports.views import TournamentViewSet, TeamViewSet, GameViewSet

router = DefaultRouter()
router.register('tournament', TournamentViewSet)
router.register('team', TeamViewSet)
router.register('game', GameViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
