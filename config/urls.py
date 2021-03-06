from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include
from sports.views import TournamentViewSet, TeamViewSet, GameViewSet
from user.views import UserViewSet

router = DefaultRouter()
router.register('tournament', TournamentViewSet)
router.register('team', TeamViewSet)
router.register('game', GameViewSet)
router.register('user', UserViewSet)

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
