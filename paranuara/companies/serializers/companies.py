"""Company serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from paranuara.companies.models import Company
from paranuara.citizens.models import Citizen

# Tasks
from paranuara.taskapp.create_employees.tasks import create_employees_by_company


class CompanyModelSerializer(serializers.ModelSerializer):
    """Company model serializer."""

    class Meta:
        """Meta class."""

        model = Company
        exclude = ['id']

    def validate(self, data):
        """Ensure both name and is_limited are present."""

        name = data.get('name', None)

        if name:
            raise serializers.ValidationError('name must be provided')
        return data


class CompanyAddEmployeesSerializer(serializers.Serializer):
    """Company associate employees serializer."""

    def validate(self, data):
        """Ensure does not have employees and there are citizens available."""

        company = self.context['company']
        citizens = Citizen.objects.filter(company=company.id)
        if len(citizens) > 0:
            raise serializers.ValidationError('This company already has emloyees')

        self.citizens = Citizen.objects.filter(company=None)
        if len(self.citizens) == 0:
            raise serializers.ValidationError('There is not citizen without company')

        return data

    def create(self, data):

        create_employees_by_company.delay(company_pk=self.context['company'].pk)
        data = {
            'msg': 'The process was released with '+str(len(self.citizens))+' citizens'
        }

        return data
