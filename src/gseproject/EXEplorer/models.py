from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cherries = models.IntegerField(default=20)
    carbonFootprint = models.IntegerField(default=5)
    pet_visible = models.BooleanField(default=True)
    next_pet_appearance = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username + "'s Profile"
      
    def printCarbonFootprint(self):
        return str(self.carbonFootprint) + " Carbon footprint value"
    
class ScannedNumber(models.Model):
    number = models.IntegerField()
    scanned_at = models.DateTimeField(auto_now_add=True)

class Tools(models.Model):
    toolsID = models.AutoField(primary_key=True, verbose_name = "Tools ID")
    toolsName = models.CharField(max_length=100, verbose_name = "Tools Name")
    toolsDescription = models.TextField(verbose_name = "Tools Description")

    def __str__(self):
        return self.toolsName

class Tree(models.Model):
    tree = models.PositiveIntegerField(default = 0, verbose_name = "tree")
    treeComebackTime = models.DateTimeField(verbose_name = "Comeback Time")
    
    def __str__(self):
        return self.tree

