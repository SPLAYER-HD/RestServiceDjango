"""Foods views."""
# Django

# Django REST Framework
from rest_framework import mixins, viewsets

# Serializers
from paranuara.foods.serializers import FoodModelSerializer

# Models
from paranuara.foods.models import Food


class FoodViewSet(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """Food view set."""
    queryset = Food.objects.all()
    serializer_class = FoodModelSerializer

    lookup_field = 'name'
