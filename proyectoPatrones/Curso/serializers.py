from rest_framework import serializers

from Curso.models import Course

image = serializers.ImageField(required=False)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["name", "start_date", "end_date", "price", "capacity", "image", "state"]