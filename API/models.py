from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
# Create your models here.

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="cars")
    plates= models.CharField(max_length=8, null=False)
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True)

    def __str__(self):
        return self.plates

