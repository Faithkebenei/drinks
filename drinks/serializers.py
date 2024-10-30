from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    # The metadata describing the model
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']

    # We now need to create an endpoint
    # Create a file inside drinks called views.py
    # Next instructions inside views.py