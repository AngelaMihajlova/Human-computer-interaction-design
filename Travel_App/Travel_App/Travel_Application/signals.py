from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
import random

from Travel_Application.models import Travel, TouristGuide

@receiver(pre_delete, sender=TouristGuide)
def my_handler(sender,instance, **kwargs):
    guides = Travel.objects.filter(touristGuide=instance.id)
    other_touristGuides = TouristGuide.objects.exclude(id=instance.id).all()

    for guide in guides:
        new_guide = random.choice(other_touristGuides)
        guide.touristGuide = new_guide
        guide.save()

