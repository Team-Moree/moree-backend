from rest_framework import serializers

from moree.models import User
from moree.enums import UserGenderEnum


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=UserGenderEnum.choices)

    class Meta:
        model = User
        read_only_fields = ("email",)
        exclude = ("status",)
