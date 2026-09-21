from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Especialidad, Paciente, Profesional, Sesion

User = get_user_model()


class ClinicaFisioterapiaAPITests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="fisioterapeuta",
            password="securepass123",
            is_staff=True,
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.especialidad = Especialidad.objects.create(
            nombre="Kinesiología",
            descripcion="Rehabilitación y movilidad.",
        )
        self.paciente = Paciente.objects.create(
            nombre="Ana",
            apellido="García",
            dni="12345678",
            email="ana@example.com",
            telefono="555123456",
            diagnostico="Dolor lumbar",
        )
        self.profesional = Profesional.objects.create(
            nombre="Luis",
            apellido="Pérez",
            email="luis@example.com",
            telefono="555654321",
            matricula="MAT-001",
            especialidad=self.especialidad,
        )
        self.sesion = Sesion.objects.create(
            paciente=self.paciente,
            profesional=self.profesional,
            fecha="2026-09-21",
            hora="09:30:00",
            duracion_minutos=60,
            observaciones="Ejercicios de movilidad",
            estado=Sesion.Estado.PENDIENTE,
        )

    def test_modelos_creados_con_str_esperado(self):
        self.assertEqual(str(self.especialidad), "Kinesiología")
        self.assertEqual(str(self.paciente), "Ana García")
        self.assertEqual(str(self.profesional), "Dr. Luis Pérez")
        self.assertIn("Ana García", str(self.sesion))

    def test_listado_de_pacientes_api(self):
        response = self.client.get("/api/fisioterapia/pacientes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["dni"], "12345678")

    def test_filtro_de_sesiones_por_estado(self):
        Sesion.objects.create(
            paciente=self.paciente,
            profesional=self.profesional,
            fecha="2026-09-22",
            hora="10:00:00",
            duracion_minutos=45,
            estado=Sesion.Estado.COMPLETADA,
        )

        response = self.client.get(
            "/api/fisioterapia/sesiones/",
            {"estado": Sesion.Estado.COMPLETADA},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["estado"], Sesion.Estado.COMPLETADA)
        self.assertEqual(len(response.data), 1)

    def test_creacion_de_sesion_via_api(self):
        payload = {
            "paciente": self.paciente.id,
            "profesional": self.profesional.id,
            "fecha": "2026-09-23",
            "hora": "11:00:00",
            "duracion_minutos": 50,
            "observaciones": "Fase inicial de rehabilitación",
            "estado": Sesion.Estado.CONFIRMADA,
        }

        response = self.client.post(
            "/api/fisioterapia/sesiones/",
            payload,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["estado"], Sesion.Estado.CONFIRMADA)
