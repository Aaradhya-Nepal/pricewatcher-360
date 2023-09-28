# serializers.py
from rest_framework import serializers
from .models import TrackerUser

class TrackerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackerUser
        fields = ['username', 'email', 'password']
