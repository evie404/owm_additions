from typing import Dict

from ...models.bone_group_mapping import BoneGroupMapping
from .default import DEFAULT_MAPPING

PHARAH_MAPPING: Dict[str, Dict[str, Dict[str, BoneGroupMapping]]] = {
    "Pharah": DEFAULT_MAPPING,
}
