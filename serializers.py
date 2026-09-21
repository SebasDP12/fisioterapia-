from rest_framework import serializers

from .models import Especialidad, Profesional, Paciente, Sesion


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ["id", "nombre", "descripcion", "created_at"]
        read_only_fields = ["id", "created_at"]


class ProfesionalSerializer(serializers.ModelSerializer):
    especialidad_nombre = serializers.CharField(
        source="especialidad.nombre",
        read_only=True,
    )

    class Meta:
        model = Profesional
        fields = [
            "id",
            "nombre",
            "apellido",
            "email",
            "telefono",
            "matricula",
            "especialidad",
            "especialidad_nombre",
            "activo",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = [
            "id",
            "nombre",
            "apellido",
            "dni",
            "email",
            "telefono",
            "fecha_nacimiento",
            "diagnostico",
            "observaciones",
            "activo",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class SesionSerializer(serializers.ModelSerializer):
    paciente_nombre = serializers.CharField(source="paciente.__str__", read_only=True)
    profesional_nombre = serializers.CharField(source="profesional.__str__", read_only=True)
    estado_display = serializers.CharField(source="get_estado_display", read_only=True)

    class Meta:
        model = Sesion
        fields = [
            "id",
            "paciente",
            "paciente_nombre",
            "profesional",
            "profesional_nombre",
            "fecha",
            "hora",
            "duracion_minutos",
            "observaciones",
            "estado",
            "estado_display",
            "created_at",
        ]
        read_only_fields = ["id", "created_at", "estado_display", "paciente_nombre", "profesional_nombre"]
