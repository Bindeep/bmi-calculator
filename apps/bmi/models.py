from django.db import models
from django.utils.functional import cached_property

from apps.bmi.utils import get_weight_group


class BMI(models.Model):
    weight = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    bmi = models.FloatField()

    @cached_property
    def weight_group(self):
        return get_weight_group(self.bmi)

    def __str__(self):
        return f'BMI of Weight: {self.weight} and Height: {self.height} is {self.bmi}'
