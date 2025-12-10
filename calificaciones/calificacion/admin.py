from django.contrib import admin
from .models import RegistroCalificacion

@admin.register(RegistroCalificacion)
class RegistroCalificacionAdmin(admin.ModelAdmin):
    list_display = ('Asignatura', 'Nota_Obtenida', 'Fecha_Evaluacion', 'N_registro')
    list_filter = ('Asignatura', 'Fecha_Evaluacion')
    search_fields = ('Asignatura',)
    ordering = ('-Fecha_Evaluacion',)
