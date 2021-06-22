import django_filters
from .models import Message

class LatLongFilter(django_filters.FilterSet):
    class Meta:
        model = Message
        fields = {
            'latitude': ['gte','lte',],
            'longitude': ['lte','gte',],
        }

