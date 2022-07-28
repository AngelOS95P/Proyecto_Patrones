from .models import Teacher

def settings(request):
    return {'settings': Teacher.load()}


    