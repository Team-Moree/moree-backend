from rest_framework import serializers

from moree.models import (
    Term,
    TermCategory
)


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        exclude = ("status",)


class TermCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TermCategory
        exclude = ("status",)
