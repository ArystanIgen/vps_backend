from django.db import models

from apps.common.enums import VPSStatuses
from apps.common.models import BaseModel


class VPSModel(BaseModel):
    class Meta:
        verbose_name = "VPS"
        verbose_name_plural = " VPS's "

    cpu = models.PositiveIntegerField(
        verbose_name='Количество Ядер',
        default=0,

    )
    ram = models.DecimalField(
        verbose_name='Объем RAM',
        max_digits=10,
        decimal_places=2,
    )
    hdd = models.DecimalField(
        verbose_name='Объем HDD',
        max_digits=10,
        decimal_places=2,
    )

    status = models.CharField(
        verbose_name='Статус Сервера',
        max_length=32,
        choices=VPSStatuses.choices,
        default=VPSStatuses.STOPPED
    )
