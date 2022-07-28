from collections import defaultdict
from pathlib import Path

import xmltodict
import json

from rest_framework import viewsets
from django.core import serializers as core_serializers
from Curso.models import Course
from Curso.serializers import CourseSerializer
from django.http import HttpResponse



class CourseViewSet (viewsets.ModelViewSet):
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer


def download_file(request):
    base_dir = Path(__file__).resolve().parent.parent
    data_dict = defaultdict(lambda: '')
    file_path = str(base_dir / "cursos.xml") #TODO: LA ESTRUCTURA DE LA RUTA CAMBIA SEGUN LA VERSION DEL DJANGO
    with open(file_path,"r") as xmlfileObj:
        data_dict = xmltodict.parse(xmlfileObj.read())
        xmlfileObj.close()
    json_str = json.dumps(data_dict)
    response = HttpResponse(json_str, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename=cursos.json'

    return response