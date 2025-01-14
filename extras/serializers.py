from rest_framework import serializers
from . import models

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'

class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Extras
        fields = '__all__'