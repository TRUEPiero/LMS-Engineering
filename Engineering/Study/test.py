from django.test import TestCase, Client
from .models import Sections_of_modules
from django.contrib.auth import get_user_model


class AuthorModelTest(TestCase):
    def setUp(self):
        self.object = Sections_of_modules.objects.create(title='Дополнительный раздел')

    def test_str12(self):
        get_user_model.
        self.assertEqual(str(self.object), 'Дополнительный раздел')

    def test_str22(self):

        self.assertEqual(str(self.object), 'Дополнительный раздел')

    def test_str13(self):
        self.assertEqual(str(self.object), 'Дополнительный раздел')

    def test_str32(self):
        self.assertEqual(str(self.object), 'Дополнительный раздел')

    def test_str(self):
        self.assertEqual(str(self.object), 'Дополнительный раздел')

    def test_str2(self):
        self.assertEqual(str(self.object), 'Дополнительный раздел')

    def tearDown(self):
        pass
