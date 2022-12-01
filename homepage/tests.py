from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm 

# Create your tests here.
def test_user_creation(self):
        # The success case.

        data = {
            'username': 'jsmith@example.com',
            'password1': 'test123',
            'password2': 'test123',
            }
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())
        u = form.save()
        self.assertEqual(repr(u), '<User: jsmith@example.com>')