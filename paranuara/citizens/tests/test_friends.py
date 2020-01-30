"""Citizens tests."""

# Django
from django.test import TestCase

# Model
from paranuara.citizens.models import Citizen
from paranuara.citizens.models import Relationship
from paranuara.companies.models import Company

# Serializers
from paranuara.citizens.serializers import SimpleCitizenModelSerializer
from paranuara.citizens.serializers import RelationshipModelSerializer

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase


class TestGetFriendsInCommon(TestCase):
    """Get Friends test case."""

    def setUp(self):
        """Test case setup."""
        self.company = Company.objects.create(
            id=1,
            name='Towers Test Company'
        )
        self.citizen1 = Citizen.objects.create(
            first_name='Diego',
            last_name='Torres',
            balance=100000,
            has_died=False,
            eyeColor='brown',
            index='9000',
            email='diegotorres@paranuara.au',
            username='diegotorres',
            password='diegotorres2020'
        )

        self.citizen2 = Citizen.objects.create(
            first_name='Fernando',
            last_name='Barrero',
            balance=100000,
            has_died=False,
            eyeColor='brown',
            index='9001',
            email='fernandobarrero@paranuara.au',
            username='fernandobarrero',
            password='fernandobarrero2020'
        )

        self.citizen3 = Citizen.objects.create(
            first_name='Thomas',
            last_name='Test',

            balance=100000,
            has_died=False,
            eyeColor='brown',
            index='9002',
            email='thomastest@paranuara.au',
            username='thomastest',
            password='thomastest2020'
        )

        self.citizen4 = Citizen.objects.create(
            first_name='Marck',
            last_name='Hivery',

            balance=100000,
            has_died=False,
            eyeColor='brown',
            index='9003',
            email='marckhivery@paranuara.au',
            username='marckhivery',
            password='marckhivery2020'
        )

        Relationship.objects.create(
            from_people=self.citizen1,
            to_people=self.citizen3
        )

        Relationship.objects.create(
            from_people=self.citizen2,
            to_people=self.citizen3
        )

        Relationship.objects.create(
            from_people=self.citizen2,
            to_people=self.citizen4
        )

    def test_friends(self):
        """ Friends relation between citizen1 and citizen2 is generated with only citizen3 in common."""
        friends_in_common = []
        relationship_list_1 = Relationship.objects.filter(from_people=self.citizen1.id)
        relationship_list_2 = Relationship.objects.filter(from_people=self.citizen2.id)

        for relationship in RelationshipModelSerializer(relationship_list_1, many=True, read_only=True).data:
            for relationship_2 in RelationshipModelSerializer(relationship_list_2, many=True, read_only=True).data:
                if (relationship_2['to_people']['has_died'] is False
                    and relationship['to_people']['id'] == relationship_2['to_people']['id']
                    and relationship_2['to_people']['eyeColor'] == 'brown'):

                    friends_in_common.append(
                        SimpleCitizenModelSerializer(relationship['to_people']).data
                    )
        #import pdb; pdb.set_trace()
        self.assertEqual(friends_in_common[0]['username'], self.citizen3.username)


class GetFriendsInCommonAPITestCase(APITestCase):
    """Friend API test case."""

    def setUp(self):
        """Test case setup."""
        self.company = Company.objects.create(
            id=1,
            name='Towers Test Company'
        )
        self.citizen1 = Citizen.objects.create(
            first_name='Diego',
            last_name='Torres',
            balance=100000,
            has_died=False,
            eyeColor='brown',
            index='9000',
            email='diegotorres@paranuara.au',
            username='diegotorres',
            password='diegotorres2020'
        )

        self.citizen2 = Citizen.objects.create(
            first_name='Fernando',
            last_name='Barrero',
            balance=100000,
            has_died=False,
            eyeColor='brown',
            index='9001',
            email='fernandobarrero@paranuara.au',
            username='fernandobarrero',
            password='fernandobarrero2020'
        )

        self.citizen3 = Citizen.objects.create(
            first_name='Thomas',
            last_name='Test',

            balance=100000,
            has_died=False,
            eyeColor='brown',
            index='9002',
            email='thomastest@paranuara.au',
            username='thomastest',
            password='thomastest2020'
        )

        self.citizen4 = Citizen.objects.create(
            first_name='Marck',
            last_name='Hivery',

            balance=100000,
            has_died=False,
            eyeColor='brown',
            index='9003',
            email='marckhivery@paranuara.au',
            username='marckhivery',
            password='marckhivery2020'
        )

        Relationship.objects.create(
            from_people=self.citizen1,
            to_people=self.citizen3
        )

        Relationship.objects.create(
            from_people=self.citizen2,
            to_people=self.citizen3
        )

        Relationship.objects.create(
            from_people=self.citizen2,
            to_people=self.citizen4
        )

        # URL
        self.url = '/citizens/friends_in_common/'

    def test_response_success(self):
        """Verify request succeed."""
        request = self.client.get(self.url, {'users':str(self.citizen1.id)+','+str(self.citizen2.id)})
        #import pdb; pdb.set_trace()
        self.assertEqual(request.status_code, status.HTTP_200_OK)
