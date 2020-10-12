from django.urls import path
from . import views

from .views import AnimalView, Animal_TypeView, Animal_PlaceView, StaffView

urlpatterns = [
    path('animal/', AnimalView.as_view()),
    path('animal/<int:pk>', AnimalView.as_view()),
    path('animal_type/', Animal_TypeView.as_view()),
    path('animal_type/<int:pk>', Animal_TypeView.as_view()),
    path('animal_place/', Animal_PlaceView.as_view()),
    path('animal_place/<int:pk>', Animal_PlaceView.as_view()),
    path('staff/', StaffView.as_view()),
    path('staff/<int:pk>', StaffView.as_view()),    
]

