import random
from unittest import TestCase
from django.urls import reverse
from rest_framework import status, response
from rest_framework.test import APITestCase
from mountain.models import Users, Coords, Level, Pereval, Image
from mountain.serializers import UserSerializer, CoordsSerializer, LevelSerializer, PerevalSerializer


class UserApiTestCase(APITestCase):
    def setUp(self):
        self.user_1 = Users.objects.create(email='pochta1@example.ru',
                                             fam='Fam1',
                                             name='Name1',
                                             otc='Otc1',
                                             phone='89210000001')
        self.user_2 = Users.objects.create(email='pochta2@example.ru',
                                             fam='Fam1',
                                             name='Name2',
                                             otc='Otc2',
                                             phone='89210000002')

    def test_get_list(self):
        url = reverse('users-list')
        response = self.client.get(url)
        serializer_data = UserSerializer([self.user_1, self.user_2], many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('users-detail', args=(self.user_1.id,))
        response = self.client.get(url)
        serializer_data = UserSerializer(self.user_1).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class CoordsApiTestCase(APITestCase):
    def setUp(self):
        self.coords_1 = Coords.objects.create(latitude='11.11', longitude='11.11', height=111)
        self.coords_2 = Coords.objects.create(latitude='22.22', longitude='22.22', height=222)

    def test_get_list(self):
        url = reverse('coords-list')
        response = self.client.get(url)
        serializer_data = CoordsSerializer([self.coords_1, self.coords_2], many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('coords-detail', args=(self.coords_1.id,))
        response = self.client.get(url)
        serializer_data = CoordsSerializer(self.coords_1).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class LevelApiTestCase(APITestCase):
    def setUp(self):
        self.lvl_1 = Level.objects.create(winter_lev='1A', spring_lev='1A', summer_lev='1A', autumn_lev='1A')
        self.lvl_2 = Level.objects.create(winter_lev='2A', spring_lev='2A', summer_lev='2A', autumn_lev='2A')

    def test_get_list(self):
        url = reverse('levels-list')
        response = self.client.get(url)
        serializer_data = LevelSerializer([self.lvl_1, self.lvl_2], many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('levels-detail', args=(self.lvl_1.id,))
        response = self.client.get(url)
        serializer_data = LevelSerializer(self.lvl_1).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(id=1, beauty_title='BTitle_1', title='BT_1', other_titles='BT_11',
                                                connect='Connects', add_time='2024-05-28T11:11:11.853Z', status='NW',
                                                tourist_id=Users.objects.create(email='pochta1@example.ru',
                                                                            fam='Fam1',
                                                                            name='Name1',
                                                                            otc='Otc1',
                                                                            phone='89210000001'),
                                                coord_id=Coords.objects.create(latitude='11.11', longitude='11.11',
                                                                                  height=111),
                                                level=Level.objects.create(winter_lev='1A', spring_lev='1A', summer_lev='1A',
                                                                           autumn_lev='1A'))
        self.pereval_2 = Pereval.objects.create(id=2, beauty_title='BTitle_2', title='BT_2', other_titles='BT_22',
                                                connect='Connects', add_time='2024-05-28T22:22:22.853Z', status='NW',
                                                tourist_id=Users.objects.create(email='pochta2@example.ru',
                                                                            fam='Fam2',
                                                                            name='Name2',
                                                                            otc='Otc2',
                                                                            phone='89210000002'),
                                                coord_id=Coords.objects.create(latitude='22.22', longitude='22.22',
                                                                                  height=222),
                                                level=Level.objects.create(winter_lev='2A', spring_lev='2A', summer_lev='2A',
                                                                           autumn_lev='2A'))

    def test_get_list(self):
        url = reverse('perevals-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('perevals-detail', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        print(serializer_data)
        print(response.data)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class UserSerializerTestCase(TestCase):
    def setUp(self):
        self.user_1 = Users.objects.create(email='pochta1@example.ru',
                                             fam='Fam1',
                                             name='Name1',
                                             otc='Otc1',
                                             phone='89210000001')
        self.user_2 = Users.objects.create(email='pochta2@example.ru',
                                             fam='Fam2',
                                             name='Name2',
                                             otc='Otc2',
                                             phone='89210000002')

    def test_check(self):
        serializer_data = UserSerializer([self.user_1, self.user_2], many=True).data
        expected_data = [

            {
                'email': 'pochta1@example.ru',
                'fam': 'Fam1',
                'name': 'Name1',
                'otc': 'Otc1',
                'phone': '89210000001'
            },
            {
                'email': 'pochta2@example.ru',
                'fam': 'Fam2',
                'name': 'Name2',
                'otc': 'Otc2',
                'phone': '89210000002'
            }
        ]
        self.assertEqual(serializer_data, expected_data)


class CoordsSerializerTestCase(TestCase):
    def setUp(self):
        self.coords_1 = Coords.objects.create(latitude='11.11111111', longitude='11.11111111', height=111)
        self.coords_2 = Coords.objects.create(latitude='22.22222222', longitude='22.22222222', height=222)

    def test_check(self):
        serializer_data = CoordsSerializer([self.coords_1, self.coords_2], many=True).data
        expected_data = [

            {
                'latitude': '11.11111111',
                'longitude': '11.11111111',
                'height': 111
            },
            {
                'latitude': '22.22222222',
                'longitude': '22.22222222',
                'height': 222
            }
        ]
        self.assertEqual(serializer_data, expected_data)


class LevelSerializerTestCase(TestCase):
    def setUp(self):
        self.lvl_1 = Level.objects.create(winter_lev='1A', spring_lev='1A', summer_lev='1A', autumn_lev='1A')
        self.lvl_2 = Level.objects.create(winter_lev='2A', spring_lev='2A', summer_lev='2A', autumn_lev='2A')

    def test_check(self):
        serializer_data = LevelSerializer([self.lvl_1, self.lvl_2], many=True).data
        expected_data = [

            {
                'winter_lev': '1A',
                'spring_lev': '1A',
                'summer_lev': '1A',
                'autumn_lev': '1A'
            },
            {
                'winter_lev': '2A',
                'spring_lev': '2A',
                'summer_lev': '2A',
                'autumn_lev': '2A'
            }
        ]
        self.assertEqual(serializer_data, expected_data)


class PerevalSerializerTestCase(TestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(beauty_title='BTitle_1', title='BT_1', other_titles='BT_11',
                                                connect='Connects1',
                                                add_time='%d-%m-%Y %H:%M:%S',
                                                status='NW',
                                                tourist_id=Users.objects.create(email='pochta1@example.ru',
                                                                            fam='Fam1',
                                                                            name='Name1',
                                                                            otc='Otc1',
                                                                            phone='89210000001'),
                                                coord_id=Coords.objects.create(latitude='11.11111111',
                                                                                  longitude='11.11111111',
                                                                                  height=111),
                                                level=Level.objects.create(winter_lev='1A', spring_lev='1A', summer_lev='1A',
                                                                           autumn_lev='1A'),
                                                )
        self.images_1 = Image.objects.create(image='image1.jpg', pereval_id=self.pereval_1, title='imagetitle1')

        self.pereval_2 = Pereval.objects.create(beauty_title='BTitle_2', title='BT_2', other_titles='BT_22',
                                                connect='Connects2',
                                                add_time='%d-%m-%Y %H:%M:%S',
                                                status='NW',
                                                tourist_id=Users.objects.create(email='pochta2@example.ru',
                                                                            fam='Fam2',
                                                                            name='Name2',
                                                                            otc='Otc2',
                                                                            phone='89210000002'),
                                                coord_id=Coords.objects.create(latitude='22.22222222',
                                                                                longitude='22.22222222',
                                                                                height=222),
                                                level=Level.objects.create(winter_lev='2A', spring_lev='2A', summer_lev='2A',
                                                                           autumn_lev='2A'))
        self.images_2 = Image.objects.create(image='image2.jpg', pereval_id=self.pereval_2, title='imagetitle2')

    def test_check(self):
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        expected_data = [
            {
                'id': self.pereval_1.id,
                'beauty_title': 'BTitle_1',
                'title': 'BT_1',
                'other_titles': 'BT_11',
                'connect': 'Connects1',
                'add_time': self.pereval_1.add_time.strftime('%d-%m-%Y %H:%M:%S'),
                'status': 'NW',
                'tourist_id': {'email': 'pochta1@example.ru', 'fam': 'Fam1', 'name': 'Name1',
                         'otc': 'Otc1', 'phone': '89210000001'},
                'coord_id': {'latitude': '11.11111111', 'longitude': '11.11111111', 'height': 111},
                'level': {'winter_lev': '1A', 'spring_lev': '1A', 'summer_lev': '1A', 'autumn_lev': '1A'},
                'images': [
                    {'image': 'image1.jpg', 'title': 'imagetitle1'},
                ]
            },
            {
                'id': self.pereval_2.id,
                'beauty_title': 'BTitle_2',
                'title': 'BT_2',
                'other_titles': 'BT_22',
                'connect': 'Connects2',
                'add_time': self.pereval_2.add_time.strftime('%d-%m-%Y %H:%M:%S'),
                'status': 'NW',
                'tourist_id': {'email': 'pochta2@example.ru', 'fam': 'Fam2', 'name': 'Name2',
                         'otc': 'Otc2', 'phone': '89210000002'},
                'coord_id': {'latitude': '22.22222222', 'longitude': '22.22222222', 'height': 222},
                'level': {'winter_lev': '2A', 'spring_lev': '2A', 'summer_lev': '2A', 'autumn_lev': '2A'},
                'images': [
                    {'image': 'image2.jpg', 'title': 'imagetitle2'},
                ]
            }
        ]

        self.assertEqual(serializer_data, expected_data)
