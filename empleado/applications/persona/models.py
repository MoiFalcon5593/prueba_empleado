from django.db import models
#
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad ', max_length=100)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural =  "Habilidades Empleado"

    def __str__(self):
        return str(self.id) +'-' + self.habilidad

# Create your models here.
class Empleado(models.Model):

    job_choices = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Ingeniero'),
        ('4', 'Otro'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres completos', max_length=120, blank= True)
    job = models.CharField('Trabajo',max_length=50, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural =  'Empleado de la empresa'
        ordering = ['first_name','last_name']
        unique_together = ['first_name']


    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
