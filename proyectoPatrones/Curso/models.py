from django.db import models

COURSE_STATES = (
    (0, 'OPEN'),
    (1, 'CLOSE'),
    (2, 'FULL')
)

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class Course (models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    capacity = models.IntegerField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    state = models.IntegerField(choices=COURSE_STATES)

    def __str__(self):
        return self.name