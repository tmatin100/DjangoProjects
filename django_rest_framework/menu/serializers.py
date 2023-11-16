# serializers needs the "rest_framework" added, under installed_apps section in settings.py

from rest_framework import serializers

from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item 
        fields = '__all__'

