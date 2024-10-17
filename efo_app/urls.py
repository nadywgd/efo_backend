from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TermViewSet, SynonymViewSet

router = DefaultRouter()
router.register(r'terms', TermViewSet)
router.register(r'synonyms', SynonymViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
