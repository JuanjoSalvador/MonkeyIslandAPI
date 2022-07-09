from django.urls import path, re_path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter
from app.views import CharactersViewSet, PiratesView, InsultsView

router = DefaultRouter()
router.register('characters', CharactersViewSet, basename='characters-view'),
router.register('pirates', PiratesView, basename='pirates-view'),
router.register('insults', InsultsView, basename='pirate-fight-view'),

urlpatterns = router.urls
