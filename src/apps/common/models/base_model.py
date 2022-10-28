import uuid

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField( # noqa
        default=uuid.uuid4, primary_key=True,
        editable=False
    )
    created_at = models.DateTimeField(
        "Дата создания",
        auto_now_add=True, blank=True,
    )

    updated_at = models.DateTimeField(
        "Дата изменения",
        auto_now=True, blank=True,
    )
