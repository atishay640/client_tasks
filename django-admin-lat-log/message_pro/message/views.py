
from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer
from .filters import LatLongFilter


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filterset_class = LatLongFilter
