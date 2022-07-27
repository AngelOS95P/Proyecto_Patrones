from rest_framework import serializers

from Curso.models import Course

image = serializers.ImageField(required=False)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'