from django.db import models

# Create your models here.
class student(models.Model):
    name= models.CharField(max_length=32)
    des= models.CharField(max_length=32)


class History(models.Model):
    name=models.CharField(max_length=32)
    des=models.CharField(max_length=32)