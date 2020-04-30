from rest_framework import serializers

from .models import Block, District, State, Ward


class StateSerializer(serializers.ModelSerializer):
    district = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = State
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    state = serializers.StringRelatedField(required=False, source="state.name")
    block = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = District
        fields = "__all__"


class BlockSerializer(serializers.ModelSerializer):
    district = serializers.IntegerField(required=False, source="dist.name")
    ward = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Block
        fields = "__all__"


class WardSerializer(serializers.ModelSerializer):
    block = serializers.StringRelatedField(required=False, source="block.name")

    class Meta:
        model = Ward
        fields = "__all__"
