from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from .models import UserAccess

#this @receiver is a decorator to receive a signal
# We have a sender which is the user that will be created and
# will send a signal of post_save and the signal is going to be received 
# by the function create_profile which has all the arguments that the post_save signal
# one of the parameter is the instance of the user(begin created) and also if the instance is (created).
# passed to it
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()     
