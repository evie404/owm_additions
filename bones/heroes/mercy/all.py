from typing import Dict

from owm_additions.bones.bone_group_mapping import BoneGroupMapping
from owm_additions.bones.heroes.mercy.atlantic import ATLANTIC_MAPPING
from owm_additions.bones.heroes.mercy.classic import CLASSIC_MAPPING
from owm_additions.bones.heroes.mercy.dr_ziegler import DR_ZIEGLER_MAPPING
from owm_additions.bones.heroes.mercy.royal_knight import ROYAL_KNIGHT_MAPPING
from owm_additions.bones.heroes.mercy.seolbim import SEOLBIM_MAPPING
from owm_additions.bones.heroes.mercy.winged_victory import WINGED_VICTORY_MAPPING
from owm_additions.bones.heroes.mercy.witch import WITCH_MAPPING
from owm_additions.bones.heroes.mercy.zhuque import ZHUQUE_MAPPING

MERCY_MAPPING: Dict[str, Dict[str, Dict[str, BoneGroupMapping]]] = {
    "Mercy": CLASSIC_MAPPING
    | ATLANTIC_MAPPING
    | DR_ZIEGLER_MAPPING
    | WINGED_VICTORY_MAPPING
    | WITCH_MAPPING
    | SEOLBIM_MAPPING
    | ZHUQUE_MAPPING
    | ROYAL_KNIGHT_MAPPING,
}
