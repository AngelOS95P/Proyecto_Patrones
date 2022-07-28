from rest_framework import serializers
from Usuario.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher.load()
        fields = ["id", "name", "lastName", "idNumber", 'email', "academicTitle", "telephone"]

