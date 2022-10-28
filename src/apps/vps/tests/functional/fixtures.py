import os
from typing import Dict, Any
from pytest import fixture

main_script_dir = os.path.dirname(__file__)


@fixture(scope='function')
def test_vps_for_create() -> Dict[str, Any]:
    return dict(
        cpu=32,
        ram=16.0,
        hdd=200.0
    )
