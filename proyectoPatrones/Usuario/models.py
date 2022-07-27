import email
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.

class Student (models.Model):
    name=models.CharField('Nombres',max_length=100)
    email = models.EmailField('Correo',max_length=50)
    birthday=models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id)

class Teacher (models.Model):
    name    =models.CharField('Nombres',max_length=100)
    email   = models.EmailField('Correo',max_length=50)
    profession  = models.CharField('Profecion',max_length=100)
    telephone   = models.CharField('Telefono',max_length=10) 

    def __str__(self):
        return str(self.id)

