from datetime import datetime
from django.db import models
from Curso.models import Course


class Inscription(models.Model):
    student = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date(datetime.now()))

    def __str__(self):
        return self.date

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        course = Course.objects.get(id=self.course.id)

        if course.max_capacity == (course.actual_capacity + 1):
            print("Curso lleno.")
            course.full_status(course.actual_capacity)
        else:
            print("Inscribiendo alumno")
            course.register_status(course.actual_capacity)
