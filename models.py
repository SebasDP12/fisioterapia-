from django.db import models


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nombre


class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    matricula = models.CharField(max_length=50, blank=True)
    especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.PROTECT,
        related_name="profesionales",
    )
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["apellido", "nombre"]
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido}"


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=50, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    diagnostico = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["apellido", "nombre"]
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Sesion(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "PENDIENTE", "Pendiente"
        CONFIRMADA = "CONFIRMADA", "Confirmada"
        COMPLETADA = "COMPLETADA", "Completada"
        CANCELADA = "CANCELADA", "Cancelada"

    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.PROTECT,
        related_name="sesiones",
    )
    profesional = models.ForeignKey(
        Profesional,
        on_delete=models.PROTECT,
        related_name="sesiones",
    )
    fecha = models.DateField()
    hora = models.TimeField()
    duracion_minutos = models.PositiveIntegerField(default=45)
    observaciones = models.TextField(blank=True)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha", "-hora"]
        verbose_name = "Sesión"
        verbose_name_plural = "Sesiones"

    def __str__(self):
        return f"{self.paciente} - {self.fecha}"
