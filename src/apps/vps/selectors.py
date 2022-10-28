from typing import Optional

import django_filters

from apps.common.exceptions import VPSNotFoundError
from apps.vps.models import VPSModel


def get_vps(
        **kwargs
) -> VPSModel:
    fetched_vps: Optional[VPSModel] = VPSModel.objects.filter(
        **kwargs
    ).first()
    if fetched_vps is None:
        raise VPSNotFoundError
    return fetched_vps


class VPSFilter(django_filters.FilterSet):
    class Meta:
        model = VPSModel
        fields = ("cpu", "status", "hdd", "ram")


def vps_list(*, filters=None):
    filters = filters or {}

    qs = VPSModel.objects.all()

    return VPSFilter(filters, qs).qs
