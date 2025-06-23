from rest_framework import serializers

from moree.models import (
    Character
)


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
