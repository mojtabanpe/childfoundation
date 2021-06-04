from django.db import models
from django.contrib.auth.models import User

class Sponser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # designation = models.CharField(max_length=50)
    # description = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    contribution = models.IntegerField()
    total_paid = models.CharField(max_length=50)
    current_saving = models.CharField(max_length=50)

    def __str__(self):
        return self.user.first_name

