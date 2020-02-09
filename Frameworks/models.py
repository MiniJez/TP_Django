from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Frameworks(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    using_percentage = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)