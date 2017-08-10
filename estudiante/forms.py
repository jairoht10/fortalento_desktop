from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    nombre = forms.CharField(
        label=_("Nombres:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'title': _("Indique los Nombres de la Persona"),
            }
        )
    )

    apellido = forms.CharField(
        label=_("Apellidos:"),
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'title': _("Indique los Apellidos de la Persona"),
            }
        )
    )

    class Meta:
        model = Estudiante
        exclude = ['user']
