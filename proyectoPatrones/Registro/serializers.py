from rest_framework import serializers

from Curso.models import Course
from Curso.serializers import CourseSerializer
from Registro.models import Inscription

image = serializers.ImageField(required=False)

class InscriptionSerializer(serializers.ModelSerializer):
    '''student = serializers.CharField(source='student.name')'''
    '''course = CourseSerializer()'''

    class Meta:
        model = Inscription
        fields = ["student", "course", "date"]
