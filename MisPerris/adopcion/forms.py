from django import forms
from .models import Perritos

class RescatesForm(forms.ModelForm):

    class Meta:
        model = Perritos
        fields = ('titulo', 'descripcion','thumb','author')
 