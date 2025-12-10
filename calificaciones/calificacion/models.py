from django.db import models
from django.contrib.auth.models import User

class RegistroCalificacion(models.Model):
    Asignatura = models.CharField(max_length=255)
    Nota_Obtenida = models.DecimalField(
        max_digits=5, 
        decimal_places=2,
        help_text="Nota obtenida en la asignatura"
    )
    Fecha_Evaluacion = models.DateField()
    N_registro = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name="Usuario"
    )
    
    def __str__(self):
        return f"{self.Asignatura} - {self.Nota_Obtenida}"
    
    class Meta:
        verbose_name = "Registro de Calificación"
        verbose_name_plural = "Registros de Calificaciones"