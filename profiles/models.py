from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.

    Fields:
    - user: OneToOneField, representing the associated user.
    - favorite_city: CharField, representing the user's favorite city.

    Meta:
    - verbose_name_plural: String, representing the plural name for the model.

    Methods:
    - __str__: Returns a string representation of the user profile.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.user.username
