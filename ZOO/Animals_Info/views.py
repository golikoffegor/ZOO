from rest_framework import viewsets

from .models import *
from .serializers import AnimalSerializer, Animal_TypeSerializer, Animal_PlaceSerializer, StaffSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

class Animal_TypeViewSet(viewsets.ModelViewSet):
    serializer_class = Animal_TypeSerializer
    queryset = Animal_Type.objects.all()

class Animal_PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = Animal_PlaceSerializer
    queryset = Animal_Place.objects.all()

class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

