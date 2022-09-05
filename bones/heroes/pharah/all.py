from typing import Dict

from ...bone_group_mapping import BoneGroupMapping
from .base import BASE_MAPPING
from .classic import CLASSIC_MAPPING
from .qinglong import QINGLONG_MAPPING
from .raptorian import RAPTORIAN_MAPPING

PHARAH_MAPPING: Dict[str, Dict[str, Dict[str, BoneGroupMapping]]] = {
    "Pharah": CLASSIC_MAPPING | QINGLONG_MAPPING | RAPTORIAN_MAPPING | BASE_MAPPING,
}
