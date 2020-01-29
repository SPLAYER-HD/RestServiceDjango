"""Food model."""

# Django
from django.db import models

# Utilities
from paranuara.utils.models import ParanuaraModel


class Food(ParanuaraModel):
    """Food model."""

    name = models.CharField(
        max_length=1000,
        blank=False
    )
    type = models.CharField(
        max_length=1000,
        blank=False
    )
    REQUIRED_FIELDS = ['name', 'type']

    def __str__(self):
        """Return name."""
        return self.name
