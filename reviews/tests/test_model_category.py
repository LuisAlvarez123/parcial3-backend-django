from django.contrib.auth import get_user_model, get_user
from django.test import TestCase
from reviews.models import Review, Movie, Category


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Drama', color='#ffffff')
        pass

    def test_nameCategory_label(self):
        data = Category.objects.get(id=1)
        field_label = data._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_nameCategory_value(self):
        data = Category.objects.get(id=1)
        self.assertEquals(data.name, 'Drama')

    def test_nameColor_label(self):
        data = Category.objects.get(id=1)
        field_label = data._meta.get_field('color').verbose_name
        self.assertEquals(field_label, 'color')

    def test_nameColor_value(self):
        data = Category.objects.get(id=1)
        self.assertEquals(data.color, '#ffffff')
