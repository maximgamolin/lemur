from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class UserPayment(models.Model):

    user = models.OneToOneField('core.User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=4)
