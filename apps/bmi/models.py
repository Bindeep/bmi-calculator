from django.db import models


class BMI(models.Model):
    weight = models.PositiveSmallIntegerField(blank=False)
    height = models.PositiveSmallIntegerField(blank=False)
    bmi = models.FloatField()

    def __str__(self):
        return f'BMI of Weight: {self.weight} and Height: {self.height} is {self.bmi}'
