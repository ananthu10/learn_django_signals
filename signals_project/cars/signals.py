from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from buyers.models import Buyers
from .models import Car

import uuid


# @receiver(pre_save, sender=Car)
# def pre_save_modify_buyer_and_create_code(sender, instance, **kargs):
#     if instance.code == "":
#         instance.code = str(uuid.uuid4()).replace("-", "").upper()[:10]
#     obj = Buyers.objects.get(user=instance.buyers.user)
#     obj.from_signals = True
#     obj.save()

@receiver(post_save, sender=Car)
def post_save_modify_buyer_and_create_code(sender, instance, created, **kargs):
    if instance.code == "":
        instance.code = str(uuid.uuid4()).replace("-", "").upper()[:10]
        instance.save()
    obj = Buyers.objects.get(user=instance.buyers.user)
    obj.from_signals = True
    obj.save()
