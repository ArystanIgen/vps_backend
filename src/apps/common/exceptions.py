from rest_framework import status
from rest_framework.exceptions import APIException


class OrganizationExistsError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Organization with the same email already exists'
    default_code = 'TaskNotFound'


class VPSNotFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "VPS not found"
    default_code = 'VPSNotFound'


class DocumentNotFoundError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Document not found"
    default_code = 'DocumentNotFound'
