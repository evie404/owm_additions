from typing import Dict, Optional, Set

from .bone_group_mapping import BoneGroupMapping
from .heroes.mercy.all import MERCY_MAPPING, MERCY_MAPPING_ALIAS
from .heroes.pharah.all import PHARAH_MAPPING

SKIN_SPECIFIC_GROUPS: Dict[str, Dict[str, Dict[str, BoneGroupMapping]]] = (
    MERCY_MAPPING | PHARAH_MAPPING
)

SKIN_ALIASES: Dict[str, Dict[str, str]] = MERCY_MAPPING_ALIAS


def get_hero_base_bone_mapping(
    character: Optional[str] = None,
) -> Dict[str, BoneGroupMapping]:
    character_mapping = SKIN_SPECIFIC_GROUPS.get(character, {})
    skin_mapping = character_mapping.get("Base", {})

    return skin_mapping


def get_skin_bone_mapping(
    character: Optional[str] = None, skin: Optional[str] = None
) -> Dict[str, BoneGroupMapping]:
    character_mapping = SKIN_SPECIFIC_GROUPS.get(character, {})
    character_aliases = SKIN_ALIASES.get(character, {})

    skin_alias = character_aliases.get(skin)
    if skin_alias:
        skin = skin_alias

    skin_mapping = character_mapping.get(skin, {})

    if len(character_mapping) == 0:
        print(f"Mapping for character `{character}` not found. Using default.")

    if len(skin_mapping) == 0:
        print(f"Mapping for skin `{skin}` not found. Using default.")

    return skin_mapping
