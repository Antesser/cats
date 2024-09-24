from .models import Cats
from rest_framework import serializers


class CatsSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Cats
        fields = ("__all__")