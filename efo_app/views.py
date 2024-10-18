from rest_framework import viewsets
from .models import Term, Synonym
from .serializers import TermSerializer, SynonymSerializer

class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all().order_by('label')
    serializer_class = TermSerializer

class SynonymViewSet(viewsets.ModelViewSet):
    queryset = Synonym.objects.all()
    serializer_class = SynonymSerializer
