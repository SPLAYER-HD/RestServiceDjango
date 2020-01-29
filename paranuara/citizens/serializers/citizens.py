"""Citizens serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from paranuara.citizens.models import Citizen
from paranuara.citizens.models import Relationship

from paranuara.foods.serializers import FoodModelSerializer


class CitizenModelSerializer(serializers.ModelSerializer):
    """Citizens model serializer."""

    favorite_food = FoodModelSerializer(many=True)

    class Meta:
        """Meta class."""
        model = Citizen
        fields = '__all__'
        depth = 1


class SimpleCitizenModelSerializer(serializers.ModelSerializer):
    """Citizens model serializer."""

    class Meta:
        """Meta class."""
        model = Citizen
        fields = ['first_name', 'last_name', 'age', 'address', 'phone']


class RelationshipModelSerializer(serializers.ModelSerializer):
    """Simple Citizens model serializer. basic fields"""

    class Meta:
        """Meta class."""
        model = Relationship
        fields = '__all__'
        depth = 1


class CitizenGetFriendsExecuteSerializer(serializers.Serializer):
    """Citizen get friends in common serializer """

    def validate(self, data):
        """Ensure is only 2 citizen to comparison."""
        if len(self.context['users']) > 2:
            raise serializers.ValidationError('This service only recive two citizens to make friends comparison')
        return data

    def create(self, data):
        users = self.context['users']
        friends_in_common = []

        relationship_list_1 = Relationship.objects.filter(from_people=users[0])
        relationship_list_2 = Relationship.objects.filter(from_people=users[1])

        for relationship in RelationshipModelSerializer(relationship_list_1, many=True, read_only=True).data:
            for relationship_2 in RelationshipModelSerializer(relationship_list_2, many=True, read_only=True).data:
                if (relationship_2['to_people']['has_died'] is False
                    and relationship['to_people']['id'] == relationship_2['to_people']['id']
                    and relationship_2['to_people']['eyeColor'] == 'brown'):

                    friends_in_common.append(
                        SimpleCitizenModelSerializer(relationship['to_people']).data
                    )

        serializer1 = SimpleCitizenModelSerializer(Citizen.objects.filter(id=users[0]), many=True, read_only=True)
        serializer2 = SimpleCitizenModelSerializer(Citizen.objects.filter(id=users[1]), many=True, read_only=True)

        if len(serializer1.data) == 0:
            raise serializers.ValidationError({"detail": "Citizen 1 does not exists"})

        if len(serializer2.data) == 0:
            raise serializers.ValidationError({"detail": "Citizen 2 does not exists"})

        citizen1 = serializer1.data[0]
        citizen2 = serializer2.data[0]

        data = {
            "user1": citizen1,
            "user2": citizen2,
            "friends_in_Common": friends_in_common
        }

        return data
