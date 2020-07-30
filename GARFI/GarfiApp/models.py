from django.db import models
from django import forms
from django.urls import reverse
from django.http import HttpResponse

# Create your models here.
class UserAccount(models.Model):

    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=234)
    email = models.EmailField(max_length=234)
    mobilenumber = models.IntegerField()
    password = models.CharField(max_length=254)
    points = models.IntegerField()

    def __str__(self):

        return self.firstname


class Code(models.Model):

    code = models.CharField(max_length=11)

    def __str__(self):

        return self.code
