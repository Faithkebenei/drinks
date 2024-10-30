# Register the different tables that we want to show up in our admin panel

from django.contrib import admin
from .models import Drink

admin.site.register(Drink)

#For next instructions go to notes.txt
