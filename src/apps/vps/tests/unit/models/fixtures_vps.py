from typing import Any, Dict
from apps.vps.models import VPSModel
from pytest import fixture


@fixture(scope='function')
def test_created_vps(
        test_vps_for_create: Dict[str, Any]
):
    created_vps: VPSModel = VPSModel(
        **test_vps_for_create
    )
    created_vps.save()
    yield created_vps
    created_vps.delete()
