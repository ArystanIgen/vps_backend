from rest_framework.test import APIClient
from typing import Dict, Any

from apps.vps.models import VPSModel


def test_vps_create_success(
        api_client: APIClient,
        test_vps_for_create: Dict[str, Any]
) -> None:
    response = api_client.post('/v1/vps/', data=test_vps_for_create)

    assert response.status_code == 201


def test_vps_list_success(
        api_client: APIClient,
        test_created_vps: VPSModel

) -> None:
    response = api_client.get('/v1/vps/')

    assert response.status_code == 200


def test_vps_get_by_id_success(
        api_client: APIClient,
        test_created_vps: VPSModel
) -> None:
    response = api_client.get(f'/v1/vps/{test_created_vps.id}/')

    assert response.status_code == 200


def test_vps_get_by_id_not_found(
        api_client: APIClient,
) -> None:
    response = api_client.get('/v1/vps/61a9e8fb-091f-496a-b9ba-3887d4379db4/')

    assert response.status_code == 404


def test_vps_get_by_id_not_valid_id(
        api_client: APIClient,
) -> None:
    response = api_client.get('/v1/vps/19230123/')

    assert response.status_code == 400


def test_vps_update_status_not_found(
        api_client: APIClient,
) -> None:
    response = api_client.put('/v1/vps/61a9e8fb-091f-496a-b9ba-3887d4379db4/')

    assert response.status_code == 404


def test_vps_update_status_success(
        api_client: APIClient,
        test_created_vps: VPSModel

) -> None:
    response = api_client.put(f'/v1/vps/{test_created_vps.id}/', status={"status": "STARTED"})

    assert response.status_code == 200
