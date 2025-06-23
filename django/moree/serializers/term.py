from rest_framework import serializers

from moree.models import (
    Term,
    TermCategory
)


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term


class TermCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TermCategory
