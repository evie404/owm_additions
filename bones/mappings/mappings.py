from typing import Dict, Optional

from .bone_group_mapping import BoneGroupMapping
from .heroes.mercy.all import MERCY_MAPPING
from .heroes.pharah.all import PHARAH_MAPPING

SKIN_SPECIFIC_GROUPS: Dict[str, Dict[str, Dict[str, BoneGroupMapping]]] = (
    MERCY_MAPPING | PHARAH_MAPPING
)


def get_hero_base_bone_mapping(
    character: Optional[str] = None,
) -> Dict[str, Dict[str, BoneGroupMapping]]:
    character_mapping = SKIN_SPECIFIC_GROUPS.get(character, {})
    skin_mapping = character_mapping.get("Base", {})

    return skin_mapping


def get_skin_bone_mapping(
    character: Optional[str] = None, skin: Optional[str] = None
) -> Dict[str, Dict[str, BoneGroupMapping]]:
    character_mapping = SKIN_SPECIFIC_GROUPS.get(character, {})
    skin_mapping = character_mapping.get(skin, {})

    if len(character_mapping) == 0:
        print(f"Mapping for character `{character}` not found. Using default.")

    if len(skin_mapping) == 0:
        print(f"Mapping for skin `{skin}` not found. Using default.")

    return skin_mapping
