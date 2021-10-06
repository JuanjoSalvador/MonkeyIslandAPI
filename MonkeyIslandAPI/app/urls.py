from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from app.views import CharactersView, PiratesView, PirateFightView

urlpatterns = [
    path('characters/', CharactersView.as_view(), name='characters-view'),
    path('pirates/', PiratesView.as_view(), name='pirates-view'),
    path('pirate_fight/', PirateFightView.as_view(), name='pirate-fight-view'),
]
