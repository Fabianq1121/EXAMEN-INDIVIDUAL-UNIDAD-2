from django.urls import path
from . import views

urlpatterns = [
    path('calificaciones/', views.listar_calificaciones, name='listar_calificaciones'),
    path('calificaciones/registrar/', views.registrar_calificacion, name='registrar_calificacion'),
]