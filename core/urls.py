from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views  import PlayerViewSet, ClubViewSet, LeagueViewSet
from . import views

router = DefaultRouter()
router.register(r'leagues', LeagueViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'clubs', ClubViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('api/', include(router.urls)),
]
