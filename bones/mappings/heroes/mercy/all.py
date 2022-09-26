from typing import Dict

from ...bone_group_mapping import BoneGroupMapping
from .atlantic import ATLANTIC_MAPPING
from .base import BASE_MAPPING
from .classic import CLASSIC_MAPPING
from .combat_medic_ziegler import COMBAT_MEDIC_ZIEGLER_MAPPING
from .devil import DEVIL_MAPPING
from .dr_ziegler import DR_ZIEGLER_MAPPING
from .dragoon import DRAGOON_MAPPING
from .pink import PINK_MAPPING
from .royal_knight import ROYAL_KNIGHT_MAPPING
from .seolbim import SEOLBIM_MAPPING
from .sugar_plum_fairy import SUGAR_PLUM_FAIRY_MAPPING
from .valkyrie import VALKYRIE_MAPPING
from .winged_victory import WINGED_VICTORY_MAPPING
from .witch import WITCH_MAPPING
from .zhuque import ZHUQUE_MAPPING

MERCY_MAPPING: Dict[str, Dict[str, Dict[str, BoneGroupMapping]]] = {
    "Mercy": ATLANTIC_MAPPING
    | BASE_MAPPING
    | CLASSIC_MAPPING
    | COMBAT_MEDIC_ZIEGLER_MAPPING
    | DEVIL_MAPPING
    | DR_ZIEGLER_MAPPING
    | DRAGOON_MAPPING
    | PINK_MAPPING
    | ROYAL_KNIGHT_MAPPING
    | SEOLBIM_MAPPING
    | SUGAR_PLUM_FAIRY_MAPPING
    | VALKYRIE_MAPPING
    | WINGED_VICTORY_MAPPING
    | WITCH_MAPPING
    | ZHUQUE_MAPPING,
}

MERCY_MAPPING_ALIAS: Dict[str, Dict[str, str]] = {
    "Mercy": {
        "Amber": "Classic",
        "Camouflage": "Classic",
        "Celestial": "Classic",
        "Cobalt": "Classic",
        "Eidgenossin": "Classic",
        "Fortune": "Classic",
        "Mist": "Classic",
        "Orchid": "Classic",
        "Snow Angel": "Classic",
        "Verdant": "Classic",
        "Mage": "Witch",
        "Sigrún": "Valkyrie",
        "Imp": "Devil",
    }
}
