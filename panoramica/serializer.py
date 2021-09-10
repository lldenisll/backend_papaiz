from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Panoramica

class PanoramicaSerializer(ModelSerializer):
    class Meta:
        model = Panoramica
        fields = ('__all__')