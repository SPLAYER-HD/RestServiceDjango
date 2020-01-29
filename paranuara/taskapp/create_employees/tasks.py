"""Celery tasks."""

# Celery
from celery.decorators import task

# models
from paranuara.companies.models import Company
from paranuara.citizens.models import Citizen


@task(name='create_employees_by_company', max_retries=2)
def create_employees_by_company(company_pk):

    company = Company.objects.filter(pk=company_pk)
    citizens = Citizen.objects.filter(company=None)

    for citizen in citizens:
        citizen.company = company[0]
        citizen.save()
