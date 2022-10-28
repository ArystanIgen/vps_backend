from drf_yasg import openapi

status_params = openapi.Parameter(
    'status',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING,
    description="VPS Status",
)

cpu_params = openapi.Parameter(
    'cpu',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_INTEGER,
    description="VPS CPU",
)

hdd_params = openapi.Parameter(
    'hdd',
    in_=openapi.IN_QUERY,
    type=openapi.FORMAT_DECIMAL,
    description="VPS HDD",
)

ram_params = openapi.Parameter(
    'ram',
    in_=openapi.IN_QUERY,
    type=openapi.FORMAT_DECIMAL,
    description="VPS RAM",
)
