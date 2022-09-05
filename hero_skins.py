from typing import Dict, List

from owm_additions.paths.skin import list_all_skins
from owm_additions.paths.victory_pose import list_all_victory_poses

HERO_SKINS: Dict[str, List[str]] = list_all_skins()
HERO_VICTORY_POSES: Dict[str, List[str]] = list_all_victory_poses()
