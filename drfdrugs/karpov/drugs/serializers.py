from rest_framework import serializers

from drugs.models import Drugs


class DrugsSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(required=False)
    class Meta:
        model = Drugs
        fields = ('title', 'description', 'group','photo')

