from django.urls import path

from apps.vps.api.views import VPSCreateAndListApi, VPSRetrieveAndUpdateApi

urlpatterns = [
    path('', VPSCreateAndListApi.as_view(), name='create-get-vps'),
    path('<str:vps_id>/', VPSRetrieveAndUpdateApi.as_view(), name='retrieve-update-vps'),
]
