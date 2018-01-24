from django.test import TestCase
from general.models import SpaUser

# models test
class SpaUserTest(TestCase):

    def create_SpaUser(self, email="email@email.com", password="jlaasociados"):
        return SpaUser.objects.create(email=email, password=password)

    def test_SpaUser_creation(self):
        miusuario = self.create_SpaUser()
        self.assertTrue(isinstance(miusuario, SpaUser))
        self.assertEqual(miusuario.__str__(), miusuario.email)