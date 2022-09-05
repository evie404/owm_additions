from typing import Dict

from owm_additions.bones.bone_group_mapping import BoneGroupMapping
from owm_additions.bones.heroes.pharah.base import BASE_MAPPING
from owm_additions.bones.heroes.pharah.classic import CLASSIC_MAPPING
from owm_additions.bones.heroes.pharah.qinglong import QINGLONG_MAPPING
from owm_additions.bones.heroes.pharah.raptorian import RAPTORIAN_MAPPING

PHARAH_MAPPING: Dict[str, Dict[str, Dict[str, BoneGroupMapping]]] = {
    "Pharah": CLASSIC_MAPPING | QINGLONG_MAPPING | RAPTORIAN_MAPPING | BASE_MAPPING,
}
