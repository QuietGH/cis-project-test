from rest_framework import serializers
from .models import Thing

class ThingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thing
        fields = ('name','length','height','width')