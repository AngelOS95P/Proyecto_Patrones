from rest_framework import serializers
from Registro.models import Inscription

image = serializers.ImageField(required=False)


class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = ["student", "course", "date"]
        read_only_fields = ["date"]
