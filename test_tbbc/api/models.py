from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phoneNumber = PhoneNumberField(region="CO")
    email = models.EmailField(max_length=75)

    def __str__(self) -> str:
        text = "{0}  {1}"
        return text.format(self.name, self.phoneNumber)
