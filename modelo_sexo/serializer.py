from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Teste

class TesteSerializer(ModelSerializer):
    class Meta:
        model = Teste
        fields = ('__all__')