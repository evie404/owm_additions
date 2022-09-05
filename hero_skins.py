from typing import Dict, List

from owm_additions.paths.animation import (
    VICTORY_POSE_ANIMATION_TYPE,
    list_all_animations,
)
from owm_additions.paths.skin import list_all_skins

HERO_SKINS: Dict[str, List[str]] = list_all_skins()
HERO_VICTORY_POSES: Dict[str, List[str]] = list_all_animations(
    VICTORY_POSE_ANIMATION_TYPE
)
