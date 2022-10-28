from pytest import fixture
from rest_framework.test import APIClient

from apps.vps.tests.functional.fixtures import *
from apps.vps.tests.unit.models.fixtures_vps import *


@fixture()
def api_client(db) -> APIClient:
    return APIClient()
