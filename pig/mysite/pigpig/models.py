from django.db import models

# Create your models here.
class Taste(models.Model):
    name = models.CharField(max_length=10, unique=True)
    english = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.name

class Cooking(models.Model):
    name = models.CharField(max_length=10, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=20, unique=True)
    tag = models.CharField(max_length=64)
    content = models.TextField()

    def __str__(self):
        return self.name