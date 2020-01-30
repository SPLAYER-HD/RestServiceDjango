"""Citizens model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# models
from paranuara.companies.models import Company

# PostgreSQL fields
from django.contrib.postgres.fields import JSONField

# Utilities
from paranuara.utils.models import ParanuaraModel


class Citizen(ParanuaraModel, AbstractUser):
    """Citizen model.
    Extend from Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    index = models.IntegerField(
         unique=True,
         default=-1
    )

    favorite_food = models.ManyToManyField(
        'foods.Food',
        related_name='favorite_food'
    )

    has_died = models.BooleanField(
        'died',
        default=False,
        help_text=(
            'Help easily distinguish citizens died or alive. '
        )
    )

    balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=None
    )

    picture = models.ImageField(
        'profile picture',
        upload_to='paranuara/citizens/pictures/',
        blank=True,
        null=True
    )

    age = models.IntegerField(
         default=-1
    )

    eyeColor = models.CharField(
        max_length=50,
        blank=False
    )

    gender = models.CharField(
        max_length=6,
        blank=True
    )

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )

    phone = models.CharField(
        validators=[phone_regex],
        max_length=20,
        blank=True
    )

    address = models.CharField(
        max_length=100,
        blank=True
    )

    company = models.ForeignKey(
        Company,
        related_name='employees_company',
        on_delete=models.SET_NULL, 
        null=True
    )

    about = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )

    greeting = models.CharField(
        max_length=1000,
        blank=True,
        null=True
    )

    tags = JSONField(
        default=None,
        blank=True,
        null=True
    )

    REQUIRED_FIELDS = ['has_died', 'eyeColor', 'index']

    def get_relations(self):
        return models.Relationship.objects.get(from_person=self)


class Relationship(models.Model):
    """Class to represent many to many relation between Ctizens"""

    from_people = models.ForeignKey(Citizen, related_name='from_people', on_delete=models.CASCADE)
    to_people = models.ForeignKey(Citizen, related_name='to_people', on_delete=models.CASCADE)
