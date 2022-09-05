from typing import Dict

from ...models.bone_group_mapping import BoneGroupMapping
from .default import DEFAULT_MAPPING
from .qinglong import QINGLONG_MAPPING

PHARAH_MAPPING: Dict[str, Dict[str, Dict[str, BoneGroupMapping]]] = {
    "Pharah": DEFAULT_MAPPING | QINGLONG_MAPPING,
}
