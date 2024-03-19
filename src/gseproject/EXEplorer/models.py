from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cherries = models.IntegerField(default=20)
    carbonFootfrint = models.IntegerField(default=5)
    # Add any other fields you need for the user profile

    def __str__(self):
        return self.user.username + "'s Profile"
    def getCarbonFootprint(self):
        return str(self.carbonFootfrint) + " Carbon footprint value"
    
class ScannedNumber(models.Model):
    number = models.IntegerField()
    scanned_at = models.DateTimeField(auto_now_add=True)