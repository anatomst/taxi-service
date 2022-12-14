from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):
    def test_manufacturer_str(self):
        manufacturer = Manufacturer.objects.create(name="Tesla", country="USA")
        self.assertEqual(str(manufacturer), "Tesla (USA)")

    def test_driver_str(self):
        driver = get_user_model().objects.create_user(
            username="test_username",
            password="test12345",
            first_name="test name",
            last_name="test last",
        )

        self.assertEqual(str(driver), f"test_username (test name test last)")

    def test_car_str(self):
        manufacturer = Manufacturer.objects.create(name="Tesla", country="USA")
        car = Car.objects.create(model="Model X", manufacturer=manufacturer)

        self.assertEqual(str(car), "Model X")

    def test_create_driver_with_license_number(self):
        username = "test_username"
        password = "test12345"
        license_number = "AAA12345"
        driver = get_user_model().objects.create_user(
            username=username, password=password, license_number=license_number
        )

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, license_number)
