from rest_framework import viewsets
from Registro.models import Inscription
from Registro.serializers import InscriptionSerializer


class InscriptionViewSet (viewsets.ModelViewSet):
    queryset = Inscription.objects.all().order_by('student')
    serializer_class = InscriptionSerializer
