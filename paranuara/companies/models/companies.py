"""Company model."""

# Django
from django.db import models

# Utilities
from paranuara.utils.models import ParanuaraModel


class Company(ParanuaraModel):

    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        unique=True,
        max_length=50,
        blank=False
    )

    def __str__(self):
        """Return name."""
        return self.name
