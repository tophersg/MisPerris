from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _

class Postulantes(models.Model):
    Correo = models.EmailField(max_length=23)
    rut = models.CharField(max_length=11)
    NombreCompleto = models.CharField(max_length=30)
    Fecha_nacimiento = models.DateField(
            default=timezone.now)
    numero = models.IntegerField()
    region = models.CharField(max_length=30)
    Comuna = models.CharField(max_length=30)
    Vivienda = models.CharField(max_length=20)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)


    def publish(self):
        
        self.save()


    def __str__(self):
        return self.rut

    class Meta:
        permissions = (
            ('postulante', _('Postulante')),
        )  

    