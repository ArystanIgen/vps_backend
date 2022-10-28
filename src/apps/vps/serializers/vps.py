from rest_framework import serializers

from apps.common.enums import VPSStatuses
from apps.vps.models import VPSModel


class VPSCreateInputSerializer(serializers.ModelSerializer):
    status = serializers.ReadOnlyField

    class Meta:
        model = VPSModel
        exclude = ("status",)


class VPSDetailOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPSModel
        fields = "__all__"


class VPSUpdateStatusInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = VPSModel
        fields = ('status',)


class VPSFilterSerializer(serializers.Serializer):
    cpu = serializers.IntegerField(required=False)
    ram = serializers.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2, )
    hdd = serializers.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2)
    status = serializers.ChoiceField(
        required=False,
        choices=VPSStatuses.choices
    )
