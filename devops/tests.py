from django.test import TestCase
from django.contrib.auth.models import User


class HelloViewTest(TestCase):
    def test_hello_page(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bonjour")
        self.assertNotContains(response, "Hello")
        self.assertNotContains(response, "Hola")


class AdminLoginTestCase(TestCase):
    def test_admin_login(self):
        username = 'admin'
        password = '123'
        admin = User.objects.create_superuser(username=username, password=password, email='admin@example.com')
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)