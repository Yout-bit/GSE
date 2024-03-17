from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0)
    # Add any other fields you need for the user profile

    def __str__(self):
        return self.user.username + "'s Profile"