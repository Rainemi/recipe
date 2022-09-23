from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField(max_length = 100)
    price = models.DecimalField(max_digits= 100000, decimal_places = 2)
    date_created = models.DateField(auto_now=True)
    how_it_looks = models.ImageField(upload_to="recipes/")

    def __str__(self):
        return self.name
