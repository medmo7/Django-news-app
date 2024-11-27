from django.test import TestCase
from django.contrib.auth import get_user_model


class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpass1234"
        )

        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(
            username="test_super", email="test_super@test.com", password="superpass1234"
        )

        self.assertEqual(super_user.username, "test_super")
        self.assertEqual(super_user.email, "test_super@test.com")
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)
