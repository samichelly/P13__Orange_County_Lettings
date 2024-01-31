from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator

class Address(models.Model):
    """
    Model representing an address.

    Fields:
    - number: PositiveIntegerField, representing the street number.
    - street: CharField, representing the street name.
    - city: CharField, representing the city name.
    - state: CharField, representing the state abbreviation.
    - zip_code: PositiveIntegerField, representing the ZIP code.
    - country_iso_code: CharField, representing the ISO code of the country.

    Meta:
    - verbose_name_plural: String, representing the plural name for the model.

    Methods:
    - __str__: Returns a string representation of the address.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.number} {self.street}"

class Letting(models.Model):
    """
    Model representing a letting.

    Fields:
    - title: CharField, representing the title of the letting.
    - address: OneToOneField, representing the address associated with the letting.

    Meta:
    - verbose_name_plural: String, representing the plural name for the model.

    Methods:
    - __str__: Returns a string representation of the letting.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Lettings"

    def __str__(self):
        return self.title
