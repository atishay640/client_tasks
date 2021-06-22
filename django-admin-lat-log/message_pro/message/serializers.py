from rest_framework import serializers

from .models import Message
from django.contrib.auth.hashers import make_password

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ("uuid",)


