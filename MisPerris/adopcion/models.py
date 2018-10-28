from django.db import models

# Create your models here.
class Perritos(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    # add in author later

    def __str__(self):
        return self.titulo

    