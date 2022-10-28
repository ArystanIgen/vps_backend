from apps.vps.models import VPSModel


def create_vps(**kwargs) -> VPSModel:
    new_vps = VPSModel(**kwargs)
    new_vps.save()
    return new_vps
