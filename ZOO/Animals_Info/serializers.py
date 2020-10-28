from rest_framework import serializers
from .models import *

class AnimalSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Animal
        fields = ('id','nickname','name','temper','age','description','created_at','updated_at')

class Animal_TypeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Animal_Type
        fields = ('id','name_id','animal_type','safe_feeding','independence','description','created_at','updated_at')

class Animal_PlaceSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Animal_Place
        fields = ('id','name','nickname_a','place_type','heat','description','created_at','updated_at')

class StaffSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Staff
        fields = ('id','name','gender','protected_animal_id','protection_time','description','created_at','updated_at')
