from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.bmi.utils import UNDERWEIGHT, HEALTHY, OVERWEIGHT, SEVERELY_OVERWEIGHT, OBESE, SEVERELY_OBESE


class BMICalculateTest(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.url = reverse('api_v1:bmi:bmi-calculate')

    def test_bmi_calculate(self):
        self.assertEqual(
            self.bmi_calculate(10, 100)['weight_group'],
            UNDERWEIGHT
        )
        self.assertEqual(
            self.bmi_calculate(20, 100)['weight_group'],
            HEALTHY
        )
        self.assertEqual(
            self.bmi_calculate(28, 100)['weight_group'],
            OVERWEIGHT
        )
        self.assertEqual(
            self.bmi_calculate(33, 100)['weight_group'],
            SEVERELY_OVERWEIGHT
        )
        self.assertEqual(
            self.bmi_calculate(38, 100)['weight_group'],
            OBESE
        )
        self.assertEqual(
            self.bmi_calculate(40, 100)['weight_group'],
            SEVERELY_OBESE
        )

    def bmi_calculate(self, weight: int, height: int) -> dict:
        data = {
            'weight': weight,
            'height': height
        }
        response = self.client.post(path=self.url, data=data, format='json')
        return response.data
