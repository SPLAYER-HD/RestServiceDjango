"""Citizens URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import citizens as citizens_views

router = DefaultRouter()
router.register(r'citizens', citizens_views.CitizenViewSet, basename='citizen')
urlpatterns = [path('', include(router.urls))]
