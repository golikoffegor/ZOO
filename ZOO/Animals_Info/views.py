from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from django_filters import rest_framework as filters

from .models import *
from .serializers import AnimalSerializer, Animal_TypeSerializer, Animal_PlaceSerializer, StaffSerializer

class AnimalView(APIView):

    def get(self, request):
        #На выходе присылает лист (список) из словарей
        animal = Animal.objects.all()
        serializer = AnimalSerializer(animal, many = True)
        return Response({"animal": serializer.data})

    def post(self, request):
        #Запрос на публикацию надо отправлять словарем
        animal = request.data.get("animal")
        serializer = AnimalSerializer(data = animal)
        if serializer.is_valid(raise_exception = True):
            animal_saved = serializer.save()
        return Response({"success": "Animal '{}' created successfully".format(animal_saved)})

    def put(self, request, pk):
        saved_animal = get_object_or_404(Animal.objects.all(), pk = pk)
        data = request.data.get('animal')
        serializer = AnimalSerializer(instance = saved_animal, data = data, partial = True)
        if serializer.is_valid(raise_exception = True):
            saved_animal = serializer.save()
        return Response({"success": "Animal '{}' updated successfully".format(saved_animal)})

    def delete(self, request, pk):
        animal = get_object_or_404(Animal.objects.all(), pk = pk)
        animal.delete()
        return Response({"message": "Animal with id `{}` has been deleted.".format(pk)}, status = 200)

class Animal_TypeView(APIView):

    def get(self, request):
        #На выходе присылает лист (список) из словарей
        animal_type = Animal_Type.objects.all()
        serializer = Animal_TypeSerializer(animal_type, many = True)
        return Response({"animal_type": serializer.data})

    def post(self, request):
        #Запрос на публикацию надо отправлять словарем
        animal_type = request.data.get("animal_type")
        serializer = Animal_TypeSerializer(data = animal_type)
        if serializer.is_valid(raise_exception = True):
            animal_type_saved = serializer.save()
        return Response({"success": "Animal_type '{}' created successfully".format(animal_type_saved)})

    def put(self, request, pk):
        saved_animal_type = get_object_or_404(Animal_Type.objects.all(), pk = pk)
        data = request.data.get('animal_type')
        serializer = Animal_TypeSerializer(instance = saved_animal_type, data = data, partial = True)
        if serializer.is_valid(raise_exception = True):
            saved_animal_type = serializer.save()
        return Response({"success": "Animal_type '{}' updated successfully".format(saved_animal_type)})

    def delete(self, request, pk):
        animal_type = get_object_or_404(Animal_Type.objects.all(), pk = pk)
        animal_type.delete()
        return Response({"message": "Animal_type with id `{}` has been deleted.".format(pk)}, status = 200)

class Animal_PlaceView(APIView):

    def get(self, request):
        #На выходе присылает лист (список) из словарей
        animal_place = Animal_Place.objects.all()
        serializer = Animal_PlaceSerializer(animal_place, many = True)
        return Response({"animal_place": serializer.data})

    def post(self, request):
        #Запрос на публикацию надо отправлять словарем
        animal_place = request.data.get("animal_place")
        serializer = Animal_PlaceSerializer(data = animal_place)
        if serializer.is_valid(raise_exception = True):
            animal_place_saved = serializer.save()
        return Response({"success": "Animal_place '{}' created successfully".format(animal_place_saved)})

    def put(self, request, pk):
        saved_animal_place = get_object_or_404(Animal_Place.objects.all(), pk = pk)
        data = request.data.get('animal_place')
        serializer = Animal_PlaceSerializer(instance = saved_animal_place, data = data, partial = True)
        if serializer.is_valid(raise_exception = True):
            saved_animal_place = serializer.save()
        return Response({"success": "Animal_place '{}' updated successfully".format(saved_animal_place)})

    def delete(self, request, pk):
        animal_place = get_object_or_404(Animal_Place.objects.all(), pk = pk)
        animal_place.delete()
        return Response({"message": "Animal_place with id `{}` has been deleted.".format(pk)}, status = 200)

class StaffView(APIView):

    def get(self, request):
        #На выходе присылает лист (список) из словарей
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many = True)
        return Response({"staff": serializer.data})

    def post(self, request):
        #Запрос на публикацию надо отправлять словарем
        staff = request.data.get("staff")
        serializer = StaffSerializer(data = staff)
        if serializer.is_valid(raise_exception = True):
            staff_saved = serializer.save()
        return Response({"success": "Staff '{}' created successfully".format(staff_saved)})

    def put(self, request, pk):
        saved_staff = get_object_or_404(Staff.objects.all(), pk = pk)
        data = request.data.get('staff')
        serializer = StaffSerializer(instance = saved_staff, data = data, partial = True)
        if serializer.is_valid(raise_exception = True):
            saved_staff = serializer.save()
        return Response({"success": "Staff '{}' updated successfully".format(saved_staff)})

    def delete(self, request, pk):
        staff = get_object_or_404(Staff.objects.all(), pk = pk)
        staff.delete()
        return Response({"message": "Staff with id `{}` has been deleted.".format(pk)}, status = 200)     

