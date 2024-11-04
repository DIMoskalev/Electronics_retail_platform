from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Link, Product
from users.models import User


class LinkTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@test.com')
        self.link = Link.objects.create(
            name='Металлургический завод',
            email='metalcreate@mail.ru',
            country='Российская Федерация',
            city='Челябинск',
            street='Ленина',
            house_number='100',
            level=1,
        )
        self.client.force_authenticate(user=self.user)

    def test_link_retrieve(self):
        url = reverse('store:link_retrieve', args=(self.link.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data.get('name'), self.link.name)

    def test_link_create(self):
        url = reverse('store:link_create')
        data = {
            'name': 'Шинный завод',
            'email': 'Chelabatires@mail.ru',
            'country': 'Российская Федерация',
            'city': 'Челябинск',
            'street': 'Пушкина',
            'house_number': '85',
            'level': 1,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Link.objects.all().count(), 2)

    def test_link_list(self):
        url = reverse('store:link_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_link_update(self):
        url = reverse('store:link_update', args=(self.link.pk,))
        data = {
            'street': 'Потапова',
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('street'), 'Потапова')

    def test_link_delete(self):
        url = reverse('store:link_delete', args=(self.link.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Link.objects.all().count(), 0)


class ProductTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.com')
        self.link = Link.objects.create(
            name='Металлургический завод',
            email='metalcreate@mail.ru',
            country='Российская Федерация',
            city='Челябинск',
            street='Ленина',
            house_number='100',
            level=1,
        )
        self.product = Product.objects.create(
            name='Обечайка',
            product_model='2',
            release_date='2024-11-04',
            supplier=self.link,
        )
        self.client.force_authenticate(user=self.user)

    def test_product_retrieve(self):
        url = reverse('store:product-detail', args=(self.product.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data.get('name'), self.product.name)

    def test_product_create(self):
        url = reverse('store:product-list')
        data = {
            'name': 'Днище',
            'product_model': '3',
            'release_date': '2024-11-04',
            'supplier': 7
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.all().count(), 2)

    def test_product_update(self):
        url = reverse('store:product-detail', args=(self.product.pk,))
        data = {
            'name': 'Донышко',
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('name'), 'Донышко')

    def test_product_delete(self):
        url = reverse('store:product-detail', args=(self.product.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.all().count(), 0)

    def test_product_list(self):
        url = reverse('store:product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
