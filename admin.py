from django.contrib import admin

from .models import Especialidad, Paciente, Profesional, Sesion


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "dni", "activo"]
    search_fields = ["nombre", "apellido", "dni"]


@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "especialidad", "activo"]
    list_filter = ["activo", "especialidad"]


@admin.register(Sesion)
class SesionAdmin(admin.ModelAdmin):
    list_display = ["paciente", "profesional", "fecha", "hora", "estado"]
    list_filter = ["estado", "fecha"]
