import os
import uuid

from django.db.models import Model, QuerySet
from django.db.models.query import RawQuerySet
from django.db.utils import DataError


def update_model_object(*,
                        model: Model,
                        refresh_updated_at: bool = True,
                        **data
                        ) -> Model:
    if refresh_updated_at:
        for field_name, field_value in data.items():
            if hasattr(model, field_name):  # pragma: no cover
                setattr(model, field_name, field_value)
        model.save()
    else:  # pragma: no cover
        update_fields = []
        for field_name, field_value in data.items():
            if hasattr(model, field_name):
                setattr(model, field_name, field_value)
                update_fields.append(field_name)
        model.save(update_fields=update_fields)
    return model


def get_first_matching_attr(obj, *attrs, default=None):
    for attr in attrs:
        if hasattr(obj, attr):
            return getattr(obj, attr)

    return default


def get_error_message(exc):
    if hasattr(exc, 'message_dict'):
        return exc.message_dict
    error_msg = get_first_matching_attr(exc, 'message', 'messages')

    if isinstance(error_msg, list):
        error_msg = ', '.join(error_msg)

    if error_msg is None:
        error_msg = str(exc)

    return error_msg


def count_queryset(*, queryset: QuerySet, filters=None) -> int:
    return queryset.count()


def count_raw_queryset(*, queryset: RawQuerySet, filters=None) -> int:
    try:
        return len(list(queryset))
    except DataError as e:
        print(e)


def calculate_readiness(*, offset: int, qs_count: int, total_qs_count: int):
    readiness = offset + qs_count
    percent = round((readiness / total_qs_count) * 100, 2)
    return percent


def get_photo_media_path(instance, filename):
    name, extension = os.path.splitext(filename)
    new_filename = '{}{}{}'.format('photos/', str(uuid.uuid4()), extension)
    return new_filename
