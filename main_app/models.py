from django.db import models
from django.urls import reverse

# Create your models here.
class Cat(models.Model):
    # models.Charfield (e.g.) are called field types; you can google others in Django
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def get_absolute_url(self):
        # self.id refers to the cat you just created
        # This redirects the user after they created or updated a cat
        return reverse('detail', kwargs={'cat_id': self.id})