from rest_framework import viewsets
from django.http import HttpResponse
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from .filters import StaffFilter

from .models import *
from .serializers import AnimalSerializer, Animal_TypeSerializer, Animal_PlaceSerializer, StaffSerializer

def set_query_params(request):
    q_fields = list(request.GET)
    q_params = dict()
    for key in q_fields:
        value = request.GET.get(key, None)
        if value:
            q_params[key] = value
    return q_params

class AnimalViewSet(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

    def get_queryset(self):
        filtered_query_set = self.queryset
        params = set_query_params(self.request)

        if "nickname" in params:
            filtered_query_set = filtered_query_set.filter(nickname = params["nickname"])

        return filtered_query_set

class Animal_TypeViewSet(viewsets.ModelViewSet):
    serializer_class = Animal_TypeSerializer
    queryset = Animal_Type.objects.all()

    def get_queryset(self):
        filtered_query_set = self.queryset
        params = set_query_params(self.request)

        if "animal_type" in params:
            filtered_query_set = filtered_query_set.filter(animal_type = params["animal_type"])

        return filtered_query_set

class Animal_PlaceViewSet(viewsets.ModelViewSet):
    serializer_class = Animal_PlaceSerializer
    queryset = Animal_Place.objects.all()

class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StaffFilter

    def get_queryset(self):
        filtered_query_set = self.queryset
        params = set_query_params(self.request)

        if "upper" in params:
            filtered_query_set = filtered_query_set.filter(protection_time__gte = params["upper"])
        if "lower" in params:
            filtered_query_set = filtered_query_set.filter(protection_time__lte = params["lower"])

        return filtered_query_set
