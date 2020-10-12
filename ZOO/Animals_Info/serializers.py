from rest_framework import serializers
from .models import *

class AnimalSerializer(serializers.Serializer): 
    nickname = serializers.CharField(max_length = 128)
    name = serializers.CharField(max_length = 128)
    temper = serializers.CharField(max_length = 128)
    age = serializers.IntegerField()
    description = serializers.CharField(max_length = 300, allow_blank = True, allow_null = True)
    created_at = serializers.DateField()
    updated_at = serializers.DateField()

    def create(self, validated_data):
        return Animal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nickname = validated_data.get('nickname', instance.nickname) 
        instance.name = validated_data.get('name', instance.name) 
        instance.temper = validated_data.get('temper', instance.temper)
        instance.age = validated_data.get('age', instance.age) 
        instance.description = validated_data.get('description', instance.description)

        instance.save()
        return instance

class Animal_TypeSerializer(serializers.Serializer): 
    name_id = serializers.IntegerField()
    animal_type = serializers.CharField(max_length = 128)
    safe_feeding = serializers.CharField(max_length = 128)
    independence = serializers.CharField(max_length = 128)
    description = serializers.CharField(max_length = 300, allow_blank = True, allow_null = True)
    created_at = serializers.DateField()
    updated_at = serializers.DateField()

    def create(self, validated_data):
        return Animal_Type.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name_id = validated_data.get('name_id', instance.name_id) 
        instance.animal_type = validated_data.get('animal_type', instance.animal_type) 
        instance.safe_feeding = validated_data.get('safe_feeding', instance.safe_feeding) 
        instance.independence = validated_data.get('independence', instance.independence) 
        instance.description = validated_data.get('description', instance.description) 

        instance.save()
        return instance

class Animal_PlaceSerializer(serializers.Serializer): 
    name = serializers.CharField(max_length = 128)
    nickname_1_id = serializers.CharField(max_length = 128, allow_blank = True, allow_null = True)
    nickname_2_id = serializers.CharField(max_length = 128, allow_blank = True, allow_null = True)
    nickname_3_id = serializers.CharField(max_length = 128, allow_blank = True, allow_null = True)
    place_type = serializers.CharField(max_length = 128)
    heat = serializers.CharField(max_length = 128)
    description = serializers.CharField(max_length = 300, allow_blank = True, allow_null = True)
    created_at = serializers.DateField()
    updated_at = serializers.DateField()

    class Meta:
        model = Animal_Place
        fields = ('name','place_type','heat','description','created_at','updated_at')

    def create(self, validated_data):
        return Animal_Place.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name) 
        instance.nickname_1_id = validated_data.get('nickname_1_id', instance.nickname_1_id) 
        instance.nickname_2_id = validated_data.get('nickname_2_id', instance.nickname_2_id) 
        instance.nickname_3_id = validated_data.get('nickname_3_id', instance.nickname_3_id) 
        instance.place_type = validated_data.get('place_type', instance.place_type) 
        instance.heat = validated_data.get('heat', instance.heat)  
        instance.description = validated_data.get('description', instance.description)   

        instance.save()
        return instance

class StaffSerializer(serializers.Serializer): 
    name = serializers.CharField(max_length = 128)
    gender = serializers.CharField(max_length = 128)
    protected_animal_id = serializers.IntegerField()
    protection_time = serializers.IntegerField()
    description = serializers.CharField(max_length = 300, allow_blank = True, allow_null = True)
    created_at = serializers.DateField()
    updated_at = serializers.DateField()

    def create(self, validated_data):
        return Staff.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name) 
        instance.gender = validated_data.get('gender', instance.gender) 
        instance.protected_animal_id = validated_data.get('protected_animal_id', instance.protected_animal_id)
        instance.protection_time = validated_data.get('protection_time', instance.protection_time)   
        instance.description = validated_data.get('description', instance.description)  

        instance.save()
        return instance


