from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner'),
)

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

# When you pass choices to a CharField, you pass a tuple of tuples and generae a select menu in our form
# Values are 'B', 'L' and 'D' - these are what will be stored in the database
# Human-readable values are 'Breakfast', 'Lunch', and 'Dinner'
class Feeding(models.Model):
    date = models.DateField('Feeding Date') # Optional
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        # Set the default value to 'B'
        default=MEALS[0][0]
    )

    # create a cat_id FK (note the _id is automatically added)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # Breakfast on 9/25
        # Dinner on 9/31
        # get_meal_display (meal is from key) provides the human-readable value
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        # Order by descending date
        ordering = ['-date']
