from rest_framework import serializers

from moree.models import (
    Store,
    StoreCategory,
    StoreCharacterPool
)


class BusinessDayMultipleChoiceField(serializers.MultipleChoiceField):
    DAYS = [
        ("Sunday", 64),
        ("Monday", 32),
        ("Tuesday", 16),
        ("Wednesday", 8),
        ("Thursday", 4),
        ("Friday", 2),
        ("Saturday", 1)
    ]
    DAY_MAP = dict(DAYS)

    def __init__(self, **kwargs):
        super().__init__(choices=[d[0] for d in self.DAYS], **kwargs)

    def to_representation(self, value):
        # int -> ["Monday", ...]
        if not isinstance(value, int):
            return value
        return [day for day, bit in self.DAYS if value & bit]

    def to_internal_value(self, data):
        # ["Monday", ...] -> int
        if not isinstance(data, list):
            self.fail("not_a_list", input_type=type(data).__name__)
        mask = 0
        for day in data:
            if day not in self.DAY_MAP:
                self.fail("invalid_choice", input=day)
            mask |= self.DAY_MAP[day]
        return mask


class StoreSerializer(serializers.ModelSerializer):
    business_day_list = BusinessDayMultipleChoiceField(write_only=True)
    business_day = BusinessDayMultipleChoiceField(read_only=True)

    class Meta:
        model = Store
        read_only_fields = ("business_day",)

    def create(self, validated_data):
        business_day = validated_data.pop("business_day_list", None)
        if business_day is not None:
            validated_data["business_day"] = business_day
        return super().create(validated_data)

    def update(self, instance, validated_data):
        business_day = validated_data.pop("business_day_list", None)
        if business_day is not None:
            validated_data["business_day"] = business_day
        return super().update(instance, validated_data)


class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCategory


class StoreCharacterPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreCharacterPool
