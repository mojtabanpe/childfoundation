import childs.models
from django.db import models
from django.contrib.auth.models import User

class Sponsor(models.Model):
    GENDER = (
        ('female', 'Female'),
        ('male', 'Male')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=10, default='female')
    total_paid = models.CharField(max_length=50, blank=True, null=True)
    current_saving = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_contribution(self):
        child_counts = childs.models.SponsoredChild.objects.filter(sponsor_id=self.pk).count()
        return str(child_counts) + ' Childs'




