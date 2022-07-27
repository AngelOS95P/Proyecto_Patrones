from django.db import models
from django_fsm import transition, FSMIntegerField

def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class STATUS_CHOICES(object):
    STATUS_OPEN = 0
    STATUS_CLOSE = 1
    STATUS_FULL = 2

class Course (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    actual_capacity = models.IntegerField()
    max_capacity = models.IntegerField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    status = FSMIntegerField(default=STATUS_CHOICES.STATUS_OPEN)

    def __str__(self):
        return self.name

    @transition(field=status, source=STATUS_CHOICES.STATUS_OPEN, target=STATUS_CHOICES.STATUS_FULL)
    def full(self, capacity):
        self.actual_capacity = capacity + 1
        self.status = 2
        self.save(update_fields=["actual_capacity", "status"])

        print("La capacidad del curso esta llena, con {} estudiantes.".format(self.actual_capacity))

    @transition(field=status, source=STATUS_CHOICES.STATUS_OPEN, target=STATUS_CHOICES.STATUS_OPEN)
    def register(self, capacity):
        self.actual_capacity = capacity + 1
        self.save(update_fields=["actual_capacity"])

        print("Inscribiendo estudiante numero {} de {}".format(self.actual_capacity, self.max_capacity))