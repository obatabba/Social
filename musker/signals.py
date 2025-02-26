from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def auto_create_profile(sender, created, instance, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

        # Have the user follow themselves
        profile.follows.set([profile])
        profile.save()