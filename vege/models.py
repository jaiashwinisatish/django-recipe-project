from django.db import models

# Create your models here.

class Recipe(models.Model):
    Recipe_name = models.CharField(max_length=100)
    Recipe_description = models.TextField()
    Recipe_image = models.ImageField(upload_to="recipes")