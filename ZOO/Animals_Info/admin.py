from django.contrib import admin
from .models import *

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'name', 'age', 'id', 'created_at', 'updated_at']

class Animal_TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'animal_type', 'id', 'created_at', 'updated_at']

class Animal_PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'place_type', 'id', 'created_at', 'updated_at']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'protected_animal', 'protection_time', 'id', 'created_at', 'updated_at']

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Animal_Type, Animal_TypeAdmin)
admin.site.register(Animal_Place, Animal_PlaceAdmin)
admin.site.register(Staff, StaffAdmin)
