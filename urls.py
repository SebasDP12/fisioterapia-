from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EspecialidadViewSet, PacienteViewSet, ProfesionalViewSet, SesionViewSet

router = DefaultRouter()
router.register(r"especialidades", EspecialidadViewSet, basename="especialidades")
router.register(r"profesionales", ProfesionalViewSet, basename="profesionales")
router.register(r"pacientes", PacienteViewSet, basename="pacientes")
router.register(r"sesiones", SesionViewSet, basename="sesiones")

urlpatterns = [
    path("", include(router.urls)),
]
