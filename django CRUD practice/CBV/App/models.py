from django.db import models
from django.urls import reverse
from django.shortcuts import render

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=254)
    mobilenumber = models.IntegerField()

    def __str__(self):

        return self.name

    def get_absolute_url(request):
        return reverse('App:displayview')
