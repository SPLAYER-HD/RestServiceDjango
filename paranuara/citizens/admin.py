"""User models admin."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from paranuara.citizens.models import Citizen


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'has_died')


admin.site.register(Citizen, CustomUserAdmin)
