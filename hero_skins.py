from typing import Dict, List

from owm_additions.paths.animation import (
    EMOTE_ANIMATION_TYPE,
    HIGHLIGHT_INTRO_ANIMATION_TYPE,
    VICTORY_POSE_ANIMATION_TYPE,
    list_all_animations,
)
from owm_additions.paths.skin import list_all_skins

HERO_SKINS: Dict[str, List[str]] = list_all_skins()
HERO_VICTORY_POSES: Dict[str, List[str]] = list_all_animations(
    VICTORY_POSE_ANIMATION_TYPE
)
HERO_HIGHLIGHT_INTROS: Dict[str, List[str]] = list_all_animations(
    HIGHLIGHT_INTRO_ANIMATION_TYPE
)
HERO_EMOTES: Dict[str, List[str]] = list_all_animations(EMOTE_ANIMATION_TYPE)
