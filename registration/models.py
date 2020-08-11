from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_choices = [('ST', 'student'), ('MGR', 'manager')]
    type = models.CharField(
        max_length=10,
        choices = type_choices,
        default = 'ST')

    def __str__(self):
        return self.user.username