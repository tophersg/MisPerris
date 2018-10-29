from django import forms
from .models import Postulantes

class PostulantesForm(forms.ModelForm):

    class Meta:
        model = Postulantes
        fields = ('Correo', 'rut','NombreCompleto','Fecha_nacimiento','numero','region','Comuna','Vivienda')
 