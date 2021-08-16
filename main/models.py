from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .teams import TEAMS

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picks = models.TextField(max_length=200, null = True)
    score = models.FloatField(default = 0)
    big_loser = models.CharField(choices=TEAMS, max_length=20, default = "Arizona Cardinals")
    nfc_champ = models.CharField(choices=TEAMS[:16], max_length=20, default = "Arizona Cardinals")
    afc_champ = models.CharField(choices=TEAMS[16:], max_length=20, default = "Buffalo Bills")
    superbowl_winner = models.CharField(choices=TEAMS, max_length=20, default = "Arizona Cardinals")

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Gamemodel(models.Model):
    team1 = models.CharField(choices=TEAMS, max_length=20, default = "Arizona Cardinals")
    team2 = models.CharField(choices=TEAMS, max_length=20, default = "Arizona Cardinals")
    points = models.FloatField(default = 0)
    winner = models.BooleanField(default = True)

    def __str__(self):
        return "{} (1) vs. {} ({})".format(self.team1, self.team2, self.points)

class General(models.Model):
    publish = models.BooleanField(default=False)
    week = models.IntegerField(default=1)

    def __str__(self):
        return 'General'

class History(models.Model):
    data = models.TextField(max_length=10000, null=True)
    week = models.IntegerField(default=1)

    def __str__(self):
        return f'week {self.week}'