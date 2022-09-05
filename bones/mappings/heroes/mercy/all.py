from typing import Dict

from ...mappings.bone_group_mapping import BoneGroupMapping
from .atlantic import ATLANTIC_MAPPING
from .classic import CLASSIC_MAPPING
from .dr_ziegler import DR_ZIEGLER_MAPPING
from .royal_knight import ROYAL_KNIGHT_MAPPING
from .seolbim import SEOLBIM_MAPPING
from .winged_victory import WINGED_VICTORY_MAPPING
from .witch import WITCH_MAPPING
from .zhuque import ZHUQUE_MAPPING

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