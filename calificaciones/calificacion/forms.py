from django import forms
from .models import RegistroCalificacion

class RegistroCalificacionForm(forms.ModelForm):
    class Meta:
        model = RegistroCalificacion
        fields = ['Asignatura', 'Nota_Obtenida', 'Fecha_Evaluacion', 'N_registro']
        widgets = {
            'Fecha_Evaluacion': forms.DateInput(attrs={'type': 'date'}),
            'Nota_Obtenida': forms.NumberInput(attrs={'step': '0.01', 'min': '0', 'max': '20'}),
        }