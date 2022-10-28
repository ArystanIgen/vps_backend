from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response

from apps.common.pagination import (LimitOffsetPagination,
                                    get_paginated_response)
from apps.common.swagger_params import (cpu_params, hdd_params, ram_params,
                                        status_params)
from apps.common.utils import update_model_object
from apps.common.views import CustomApiView
from apps.vps.models import VPSModel
from apps.vps.selectors import get_vps, vps_list
from apps.vps.serializers import (VPSCreateInputSerializer,
                                  VPSDetailOutputSerializer,
                                  VPSFilterSerializer,
                                  VPSUpdateStatusInputSerializer)
from apps.vps.services import create_vps


class VPSCreateAndListApi(CustomApiView):
    api_description = 'создать VPS'

    @swagger_auto_schema(
        operation_summary="VPSCreate",
        operation_description=api_description,
        operation_id="VPSCreate",
        responses={status.HTTP_201_CREATED: VPSDetailOutputSerializer()},
        request_body=VPSCreateInputSerializer,

    )
    def post(self, request):
        serializer = VPSCreateInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        new_vps: VPSModel = create_vps(**serializer.data)
        data = VPSDetailOutputSerializer(new_vps).data
        return Response(data=data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="VPSListRetrieve",
        operation_description=api_description,
        operation_id="VPSListRetrieve",
        manual_parameters=[
            cpu_params,
            ram_params,
            hdd_params,
            status_params
        ],
        responses={status.HTTP_200_OK: VPSDetailOutputSerializer(many=True)}
    )
    def get(self, request):
        filters_serializer = VPSFilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        fetched_vps_list = vps_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=LimitOffsetPagination,
            serializer_class=VPSDetailOutputSerializer,
            queryset=fetched_vps_list,
            request=request,
            view=self
        )


class VPSRetrieveAndUpdateApi(CustomApiView):
    api_description = 'получить VPS по ID'

    @swagger_auto_schema(
        operation_summary="VPSRetrieve",
        operation_description=api_description,
        operation_id="VPSRetrieve",
        responses={status.HTTP_200_OK: VPSDetailOutputSerializer()}
    )
    def get(self, request, vps_id):
        fetched_vps: VPSModel = get_vps(id=vps_id)

        data = VPSDetailOutputSerializer(fetched_vps).data

        return Response(data=data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="VPSnUpdateStatus",
        operation_description=api_description,
        operation_id="VPSnUpdateStatus",
        responses={status.HTTP_200_OK: VPSDetailOutputSerializer()},
        request_body=VPSUpdateStatusInputSerializer,

    )
    def put(self, request, vps_id):
        serializer = VPSUpdateStatusInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        fetched_vps: VPSModel = get_vps(id=vps_id)
        update_model_object(
            model=fetched_vps,
            refresh_updated_at=True,
            **serializer.data
        )
        data = VPSDetailOutputSerializer(fetched_vps).data
        return Response(data=data, status=status.HTTP_200_OK)
