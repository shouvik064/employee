from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    age = models.IntegerField(blank=True,null=True)
    post = models.CharField(max_length=200,blank=False, default='')
