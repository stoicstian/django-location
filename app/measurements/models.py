from operator import mod
from django.db import db, models
from django.db.models import CharField


# Create your models here.
# class Measurement(models.Model):
#     """Modelo de medidas de un punto a otro."""

#     location = models.CharField(max_length=200)
#     destination = models.CharField(max_length=200)
#     distance = models.DecimalField(
#         max_digits=10, decimal_places=2, verbose_name="Distancia en Km"
#     )

#     def __str__(self) -> str:
#         """Representación clase en formato texto."""
#         return (
#             f"Distance from {self.location} "
#             + "to {self.destination} is {self.distance}"
#         )
class Family(models.Model):
    """Clase familia."""

    nombre = models.CharField("nombre familia", max_length=20)

    class Meta:
        """Clase Meta."""

        ordering = ["nombre"]
        db_table = "familia_db"
        verbose_name = "Familia"
        verbose_name_plural = "Familias"

    def __str__(self) -> str:
        """Método string."""
        return self.nombre


class Person(models.Model):
    """Clase persona."""

    class Meta:
        """Clase Meta."""

        pass

    SexoType = models.TextChoices(
        "Sexo",
        "Femenino Masculino",
    )

    nombre = models.CharField(
        "nombre de la persona",
        max_length=30,
    )

    apellido = models.CharField(
        "apellido de la persona",
        max_length=30,
    )

    familia = models.ForeignKey(
        Family,
        on_delete=models.CASCADE,
        null=True,
    )

    documento = models.IntegerField(
        "cédula de ciudadanía",
        default=0000000,
    )

    sexo = models.CharField(
        blank=True,
        choices=SexoType.choices,
        max_length=10,
    )

    def __str__(self) -> str:
        """Método string."""
        return f"{self.nombre} {self.apellido}"
