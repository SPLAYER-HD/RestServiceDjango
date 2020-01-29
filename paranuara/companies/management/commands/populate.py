# Command to populate table employes

import json
import os

# Django
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

# models
from paranuara.companies.models import Company
from paranuara.citizens.models import Citizen
from paranuara.citizens.models import Relationship
from paranuara.foods.models import Food


class Command(BaseCommand):
    help = 'Populate Companies and Citizens  from json'

    def add_arguments(self, parser):
        parser.add_argument('json', nargs='+', type=str)
        parser.add_argument('model', nargs='+', type=str)

    def handle(self, *args, **options):

        entity_list = json.load(open(os.getcwd()+'/resources/'+options['json'][0]))
        if options['model'][0] == 'company':
            for company in entity_list:
                try:
                    Company.objects.create(
                        id=company['index'],
                        name=company['company']
                    )
                except IntegrityError as error:
                    self.stdout.write(self.style.ERROR(str(error) + ' Company "%s"' % company['company']))

        elif options['model'][0] == 'person':
            for person in entity_list:
                # Get Company
                company = Company.objects.filter(id=person['company_id'])

                if(len(company) == 0):
                    self.stdout.write(
                        self.style.WARNING('Warning company with id %i does not exists ' % person['company_id'])
                    )
                    self.stdout.write(
                        self.style.WARNING('Citizen without company associated: "%s"' % person['name'])
                    )
                    company = None
                else:
                    company = company[0]

                # Load Favorite food
                citizen_favorate_food = []
                for favorite_food in person['favouriteFood']:
                    try:
                        type = 'Fruit'
                        food = Food.objects.filter(name=favorite_food)
                        if len(food) == 0:
                            food_list = json.load(open(os.getcwd()+'/resources/food_clasification.json'))
                            for f in food_list:
                                if f['name'] == favorite_food:
                                    __type = f['type']
                                    break
                            if __type:
                                type = __type
                            food = Food.objects.create(
                                name=favorite_food,
                                type=type,
                            )
                        else:
                            food = food[0]
                        citizen_favorate_food.append(food)
                    except IntegrityError as error:
                        self.stdout.write(self.style.ERROR(str(error) + ' Association of Food "%s"' % person['name']))
                try:
                    citizen = Citizen.objects.create(
                        has_died=person['has_died'],
                        balance=(person['balance'].replace('$', '').replace(',', '')),
                        picture=person['picture'],
                        age=person['age'],
                        eyeColor=person['eyeColor'],
                        gender=person['gender'],
                        email=person['email'],
                        username=person['name'].split(" ")[0]+'_'+person['name'].split(" ")[1],
                        phone=person['phone'],
                        address=person['address'],
                        about=person['about'],
                        tags=person['tags'],
                        company=company,
                        greeting=person['greeting'],
                        first_name=person['name'].split(" ")[0],
                        last_name=person['name'].split(" ")[1],
                        index=person['index']
                    )
                    citizen.favorite_food.set(citizen_favorate_food)

                except IntegrityError as error:
                    self.stdout.write(self.style.ERROR(str(error) + ' Citizen "%s"' % person['name']))

            # Load relationship
            for person in entity_list:
                try:
                    from_people = Citizen.objects.filter(index=person['index'])[0]
                    for friend in person['friends']:
                        to_people = Citizen.objects.filter(index=friend['index'])[0]
                        Relationship.objects.create(
                            from_people=from_people,
                            to_people=to_people
                        )

                except IntegrityError as error:
                    self.stdout.write(self.style.ERROR(str(error) + ' Relationship "%s"' % person['index']))

        self.stdout.write(self.style.SUCCESS('Ending insert data from  '+options['json'][0]))
