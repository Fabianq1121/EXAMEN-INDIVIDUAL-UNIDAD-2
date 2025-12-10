from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import RegistroCalificacion
from .forms import RegistroCalificacionForm

# Vista para listar calificaciones
def listar_calificaciones(request):
    calificaciones = RegistroCalificacion.objects.all()
    return render(request, 'calificacion/listar.html', {
        'calificacion': calificaciones
    })

# Vista para registrar nueva calificación
def registrar_calificacion(request):
    if request.method == 'POST':
        form = RegistroCalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_calificacion')
    else:
        form = RegistroCalificacionForm()
    
    return render(request, 'calificacion/registrar.html', {
        'form': form
    })
