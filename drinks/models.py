# To tell django that this is a model, we need to inherit from a model class as shown in the two lines of code below
from django.db import models

# Describing what every drink should look like
class Drink(models.Model): 
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=500)

    #To not return an object but actual values in the admin panel
    def __str__(self):
        return self.name + ' ' + self.description


# To create a database from this table, we need to create another migration
# Command: python manage.py makemigrations drinks
# To fix the error that occurs add the name above 'drinks' to INSTALLED_APPS inside settings.py
# Apply unapplied migrations to the database
#Command: python manage.py migrate
# Inside the drinks directory, create a admin.py file