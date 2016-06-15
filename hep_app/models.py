from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class SavedCalculation(models.Model):
    entry_one = models.FloatField()
    entry_two = models.FloatField()
    math = models.CharField(max_length=2)
    result = models.FloatField()
    math_user = models.ForeignKey(User)
