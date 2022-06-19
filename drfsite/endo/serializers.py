from rest_framework import serializers

from .models import Endo


class EndoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endo
        fields = ('name','surname','cat')