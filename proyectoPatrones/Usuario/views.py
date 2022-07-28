from rest_framework import viewsets
from Usuario.models import Teacher
from Usuario.serializers import TeacherSerializer

# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().order_by('name')
    serializer_class = TeacherSerializer
