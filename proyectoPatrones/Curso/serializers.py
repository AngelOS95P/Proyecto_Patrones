from rest_framework import serializers

from Curso.models import Course

image = serializers.ImageField(required=False)


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "name", "start_date", "end_date", 'price', "max_capacity", "image", "actual_capacity", "status"]
        read_only_fields = ["status", "actual_capacity"]
