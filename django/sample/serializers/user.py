from rest_framework import serializers

from sample.models import User
from sample.enums import UserGenderEnum


class UserSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=UserGenderEnum.choices)

    class Meta:
        model = User
        read_only_fields = ("email",)
        exclude = ("status",)
