from rest_framework import viewsets
from Curso.models import Course
from Curso.serializers import CourseSerializer


class CourseViewSet (viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer
