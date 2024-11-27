from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


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


class SignupPageTests(TestCase):

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.first().username, "testuser")
        self.assertEqual(get_user_model().objects.first().email, "testuser@email.com")
