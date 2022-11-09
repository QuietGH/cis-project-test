from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ThingSerializer
from .models import Thing

# Create your views here.

class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all().order_by('name')
    serializer_class = ThingSerializer