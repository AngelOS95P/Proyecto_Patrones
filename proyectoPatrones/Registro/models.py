from datetime import datetime
from pyexpat import model
from django.db import models
from Curso.models import Course
from Usuario.models import Student


class Inscription(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date(datetime.now()))

    def __str__(self):
        return self.date

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        course = Course.objects.get(id=self.course.id)
        student =Student.objects.get(id=self.save_base.id)

        if course.max_capacity == (course.actual_capacity + 1):
            print("Curso lleno.")
            course.full_status(course.actual_capacity)
        else:
            print("Inscribiendo alumno")
            course.register_status(course.actual_capacity)
