"""Company views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from paranuara.companies.serializers import CompanyModelSerializer
from paranuara.companies.serializers import CompanyAddEmployeesSerializer
from paranuara.citizens.serializers import CitizenModelSerializer

# Models
from paranuara.companies.models import Company
from paranuara.citizens.models import Citizen


class CompanyViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """Company view set."""

    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer

    lookup_field = 'name'
    search_fields = ('name')
    ordering_fields = ('name')

    @action(detail=True, methods=['get'])
    def employees(self, request, *args, **kwargs):
        company = self.get_object()

        citizens = Citizen.objects.filter(company=company.id)
        data = {
            'employees': CitizenModelSerializer(citizens, many=True).data
        }
        if len(citizens) == 0:
            data['to_load_unemployee_citizens'] = 'http://localhost:8000/companies/'+str(company)+'/add_free_employees/'
        return Response(data)

    @action(detail=True, methods=['post'])
    def add_free_employees(self, request, *args, **kwargs):
        """Company add employees."""
        company = self.get_object()

        serializer = CompanyAddEmployeesSerializer(
            data=request.data, context={'company': company}
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response(data, status=status.HTTP_200_OK)
