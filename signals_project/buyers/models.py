from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Buyers(models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE)
    from_signals = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
