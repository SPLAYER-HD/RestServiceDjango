"""Foods URLs."""

# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import foods as foods_views

router = DefaultRouter()
router.register(r'foods', foods_views.FoodViewSet, basename='food')
urlpatterns = [path('', include(router.urls))]
