from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Especialidad, Profesional, Paciente, Sesion
from .serializers import (
    EspecialidadSerializer,
    ProfesionalSerializer,
    PacienteSerializer,
    SesionSerializer,
)


class EspecialidadViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    permission_classes = [IsAuthenticated]


class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.select_related("especialidad").all()
    serializer_class = ProfesionalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        nombre = self.request.query_params.get("nombre")
        apellido = self.request.query_params.get("apellido")
        especialidad = self.request.query_params.get("especialidad")
        activo = self.request.query_params.get("activo")

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)
        if especialidad:
            queryset = queryset.filter(especialidad_id=especialidad)
        if activo is not None:
            queryset = queryset.filter(activo=activo.lower() == "true")
        return queryset


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        nombre = self.request.query_params.get("nombre")
        apellido = self.request.query_params.get("apellido")
        dni = self.request.query_params.get("dni")
        activo = self.request.query_params.get("activo")

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if apellido:
            queryset = queryset.filter(apellido__icontains=apellido)
        if dni:
            queryset = queryset.filter(dni__icontains=dni)
        if activo is not None:
            queryset = queryset.filter(activo=activo.lower() == "true")
        return queryset


class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.select_related("paciente", "profesional").all()
    serializer_class = SesionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset
        paciente = self.request.query_params.get("paciente")
        profesional = self.request.query_params.get("profesional")
        estado = self.request.query_params.get("estado")
        fecha = self.request.query_params.get("fecha")

        if paciente:
            queryset = queryset.filter(paciente_id=paciente)
        if profesional:
            queryset = queryset.filter(profesional_id=profesional)
        if estado:
            queryset = queryset.filter(estado=estado)
        if fecha:
            queryset = queryset.filter(fecha=fecha)
        return queryset
