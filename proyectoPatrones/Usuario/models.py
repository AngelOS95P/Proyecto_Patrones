import email
from pyexpat import model
from statistics import mode
from django.db import models
from django.core.cache import cache

class TeacherBaseModel (models.Model):
    class Meta:
        abstract = True

    def set_cache(self):
        cache.set(self.__class__.__name__,self)
    
    def delete(self, *args, **kwarhs):
        pass
    
    def save(self, *args, **kwargs):
        self.pk = 1
        super (TeacherBaseModel, self).save(*args, **kwargs)
        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created =cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class Teacher (TeacherBaseModel):
    name    =models.CharField('Nombres',max_length=30,default='Pedro')
    lastName=models.CharField('Apellido',max_length=30,default='Cordero')
    idNumber=models.CharField('Cedula',max_length=10,default='0105913891')
    email   = models.EmailField('Correo',max_length=50, default='pedro@ups.edu.ec')
    academicTitle  = models.CharField('Titulo academico',max_length=100,default='Ingeniero de Sistemas')
    telephone   = models.CharField('Telefono',max_length=10,default='0987654321') 



class Student (models.Model):
    name=models.CharField('Nombres',max_length=100)
    email = models.EmailField('Correo',max_length=50)
    birthday=models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.id)
