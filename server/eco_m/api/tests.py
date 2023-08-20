from django.contrib.auth import login
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from rest_framework.test import APITestCase

from client.models import Client as C


class BaseServices(APITestCase):
    def setUp(self) -> None:
        self.maxDiff = None

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.c = C.objects.create(
            user=self.user,
        )

        self.client = Client()
        self.client.force_login(self.user)

    def test_post_with_min_info(self):
        url = reverse("sender-list")
        response = self.client.post(
            url,
            data=dict(
                message="Test",
                email="Test@mail.com",
                phone="+375 (45) 434-62-46",
            ),
        )
        result = {"message": "Success"}

        self.assertEquals(response.data, result)
        self.assertEquals(response.status_code, 201)