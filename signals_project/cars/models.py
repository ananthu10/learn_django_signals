from django.db import models
from buyers.models import Buyers
# Create your models here.

import uuid


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    buyers = models.ForeignKey(Buyers, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.name}-{self.price}-{self.buyers}"

   #  def save(self, *args, **kwargs):
   #      if self.code == "":
   #          self.code = str(uuid.uuid4()).replace("-", "").upper()[:10]
   #      return super().save(*args, **kwargs)
 # traditinal method to crete pre save
