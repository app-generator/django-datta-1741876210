# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    phone = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Event(models.Model):

    #__Event_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Event_FIELDS__END

    class Meta:
        verbose_name        = _("Event")
        verbose_name_plural = _("Event")


class Ticket(models.Model):

    #__Ticket_FIELDS__
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    #__Ticket_FIELDS__END

    class Meta:
        verbose_name        = _("Ticket")
        verbose_name_plural = _("Ticket")



#__MODELS__END
