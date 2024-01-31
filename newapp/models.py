from django.db import models

# Create your models here.
class Member(models.Model):
    fullname=models.CharField(max_length=100)
    section=models.CharField(max_length=100)
    year=models.CharField(max_length=100)