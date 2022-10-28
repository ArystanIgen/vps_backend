from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from config.settings.components.common import DEBUG, MEDIA_ROOT, MEDIA_URL
from config.settings.components.schemas import SchemaGenerator

api_urlpatterns = [

    path('vps/', include('apps.vps.api.urls'), name="VPS"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(
        (api_urlpatterns, 'admin_api_urlpatterns'),
        namespace='admin_api_urlpatterns')),
]

urlpatterns += tuple(
    static(prefix=MEDIA_URL, document_root=MEDIA_ROOT),
)

if DEBUG:
    import debug_toolbar

    schema_view = get_schema_view(
        openapi.Info(
            title="VPS API",
            default_version='v1',
            description="VPS api description",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="contact@snippets.local"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
        patterns=api_urlpatterns,
        generator_class=SchemaGenerator,
    )

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
        path(
            'swagger/',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui',
        )
    ]
