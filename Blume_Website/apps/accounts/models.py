from django.db import models
from django.contrib.auth.models import User

class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

# a persona for a user such as DIY, hacker, representative, etc.
class UserPersona(models.Model):  # system generated - users can't define persona themselves aka add to the table, only admin (me) can
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):  # allows user to provide their persona
        return self.name


# Create your models here.
class UserProfile(models.Model):  # reference a particular user
    # owner - used by Foreign key
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")  # on_delete will delete anything associated to user

    # settings
    is_full_name_displayed = models.BooleanField(default=True)

    # details
    bio = models.CharField(max_length=500, blank=True, null=True)  # allows field to be blank and null when set to True in database
    website = models.URLField(max_length=200, blank=True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)  # multiple users can point at the same persona, so we use a foreign key
    interests = models.ManyToManyField(UserInterest, blank=True) #ManyToMany by default is empty array of references
