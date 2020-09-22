from django.db import models


# Create your models here.
class Departamento(models.Model):
    name = models.CharField('nombre', max_length=100)
    shor_name = models.CharField('Nombre corto', max_length=20, unique= True)
    anulate = models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural =  "Areas de empresa"
        ordering = ['name']
        unique_together = ['name','shor_name']


    def __str__(self):
        return str(self.id) +'-' + self.name + '-' + self.shor_name