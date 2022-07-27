from datetime import datetime
from django.db import models
from django_fsm import transition, FSMIntegerField


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class STATUS(object):
    STATUS_OPEN = 0
    STATUS_CLOSE = 1
    STATUS_FULL = 2


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.IntegerField()
    actual_capacity = models.IntegerField(default=0)
    max_capacity = models.IntegerField()
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    status = FSMIntegerField(default=STATUS.STATUS_OPEN)

    def __str__(self):
        return self.name

    def is_out_date(self):
        now = datetime.date(datetime.now())

        if self.start_date <= now <= self.end_date:
            return False
        else:
            return True

    def is_in_date(self):
        now = datetime.date(datetime.now())
        return self.start_date <= now <= self.end_date

    @transition(field=status, source=STATUS.STATUS_OPEN, target=STATUS.STATUS_CLOSE,
                conditions=[is_out_date])
    def close_status(self):
        self.status = 1

        print("El curso ha sido cambiado al estado CERRADO - codigo {}  .".format(self.status))

    @transition(field=status, source=STATUS.STATUS_CLOSE, target=STATUS.STATUS_OPEN,
                conditions=[is_in_date])
    def open_status(self):
        self.status = 0

        print("El curso ha sido cambiado al estado ABIERTO - codigo {}  .".format(self.status))

    @transition(field=status, source=STATUS.STATUS_OPEN, target=STATUS.STATUS_FULL)
    def full_status(self, capacity):
        self.actual_capacity = capacity + 1
        self.status = 2
        self.save(update_fields=["actual_capacity", "status"])

        print("La capacidad del curso esta llena, con {} estudiantes, se cambia al estado FULL.".format(
            self.actual_capacity))

    @transition(field=status, source=STATUS.STATUS_OPEN, target=STATUS.STATUS_OPEN)
    def register_status(self, capacity):
        self.actual_capacity = capacity + 1
        self.save(update_fields=["actual_capacity"])

        print("Inscribiendo estudiante numero {} de {}, estado ABIERTO".format(self.actual_capacity, self.max_capacity))

    def save(self, *args, **kwargs):
        if self.is_out_date() and self.status == 0:
            self.close_status()

        if self.is_in_date() and self.status == 1:
            self.open_status()

        super().save(*args, **kwargs)
