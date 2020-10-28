from django_filters import rest_framework as filters
from .models import Staff

class StaffFilter(filters.FilterSet):
    class Meta:
        model = Staff
        fields = {'protection_time': ['gt', 'lt'],
            }