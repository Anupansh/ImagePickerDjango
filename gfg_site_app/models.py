from django.db import models

# Create your models here.

class Students(models.Model):
    diploma = models.FileField(null=True)
