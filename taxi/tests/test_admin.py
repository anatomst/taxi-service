from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

TAXI_ADMIN_DRIVER_LIST_URL = "http://127.0.0.1:8000/admin/taxi/driver/"


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin", password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.driver = get_user_model().objects.create_user(
            username="driver", password="driver12345", license_number="AAA12345"
        )

    def test_driver_license_number_listed(self):
        """Tests that driver's license number is in list_display on driver admin page"""
        url = TAXI_ADMIN_DRIVER_LIST_URL
        res = self.client.get(url)

        self.assertContains(res, self.driver.license_number)

    def test_driver_detail_license_number_listed(self):
        """Tests that driver's license number is on driver detail admin page"""
        url = f"{TAXI_ADMIN_DRIVER_LIST_URL}{self.driver.id}/change/"
        res = self.client.get(url)

        self.assertContains(res, self.driver.license_number)
