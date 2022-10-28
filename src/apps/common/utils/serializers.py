from rest_framework import serializers


def create_serializer_class(name, fields):
    return type(name, (serializers.Serializer,), fields)  # pragma: no cover


def inline_serializer(*,
                      fields,
                      data=None,
                      **kwargs):
    serializer_class = create_serializer_class(name='', fields=fields)  # pragma: no cover

    if data is not None:  # pragma: no cover
        return serializer_class(data=data, **kwargs)

    return serializer_class(**kwargs)  # pragma: no cover
