from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@amir', password='testpass'):
    """create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """ test creating a new user with an email is successful"""
        email = "test@amir.com"
        password = "testpass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalized(self):
        """normalize email entered"""
        email = "test@AMIR.COM"
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test Creating use with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """test a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@amir.com',
            "test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan',
        )

        self.assertEqual(str(tag), tag.name)
