from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


