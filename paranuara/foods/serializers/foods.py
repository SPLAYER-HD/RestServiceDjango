"""Food serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from paranuara.foods.models import Food


class FoodModelSerializer(serializers.ModelSerializer):
    """Food model serializer."""

    class Meta:
        """Meta class."""

        model = Food
        fields = '__all__'


class FoodByTypeModelSerializer(serializers.ModelSerializer):
    """Food model serializer."""

    class Meta:
        """Meta class."""

        model = Food
        fields = '__all__'
