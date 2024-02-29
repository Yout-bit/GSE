from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    def setUp(self):
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com',
        }

    def test_signup_view(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)

    def test_signup_success(self):
        response = self.client.post(self.signup_url, data={
            'username': self.user_data['username'],
            'email': self.user_data['email'],
            'password1': self.user_data['password'],
            'password2': self.user_data['password']
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_signup_failure(self):
        invalid_data = {'username': '', 'password1': 'password123', 'password2': 'password321', 'email': 'invalidemail'}
        response = self.client.post(self.signup_url, data=invalid_data)
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login.html')

    def test_login_success(self):
        User.objects.create_user(**self.user_data)

        response = self.client.post(self.login_url, data={'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('home'))

    def test_login_failure(self):
        response = self.client.post(self.login_url, data={'username': 'nonexistentuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
