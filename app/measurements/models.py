from django.db import models


# Create your models here.
class Measurement(models.Model):
    """Modelo de medidas de un punto a otro."""

    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Distancia en Km"
    )

    def __str__(self) -> str:
        """Representación clase en formato texto."""
        return (
            f"Distance from {self.location} "
            + "to {self.destination} is {self.distance}"
        )