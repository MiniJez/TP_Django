from django.db import models

# Create your models here.
class Frameworks(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    using_percentage = models.PositiveIntegerField()