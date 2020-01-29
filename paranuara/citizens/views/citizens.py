"""Citizens views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from paranuara.citizens.serializers import CitizenModelSerializer
from paranuara.citizens.serializers import CitizenGetFriendsExecuteSerializer

# Models
from paranuara.citizens.models import Citizen


class CitizenViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """Citizen view set."""

    queryset = Citizen.objects.all()
    serializer_class = CitizenModelSerializer

    lookup_field = 'id'
    ordering_fields = ('name')

    @action(detail=True, methods=['get'])
    def get_food(self, request, *args, **kwargs):
        """Citizens get Food."""
        citizen = self.get_object()
        serializer = CitizenModelSerializer(citizen)
        fruits = []
        vegetables = []
        for food in serializer.data['favorite_food']:
            if food['type'] == 'Fruit':
                fruits.append(food['name'])
            else:
                vegetables.append(food['name'])
        data = {
           "username": serializer.data['username'],
           "age": serializer.data['age'],
           "fruits": fruits,
           "vegetables": vegetables
        }

        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def friends_in_common(self, request, *args, **kwargs):
        """Citizens get friends in common."""

        serializer = CitizenGetFriendsExecuteSerializer(
            data=request.data, context={'users': request.query_params.get('users').split(',')}
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        return Response(data, status=status.HTTP_200_OK)
