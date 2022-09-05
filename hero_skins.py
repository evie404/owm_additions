from typing import Dict, List

from owm_additions.paths.skin import list_all_skins

HERO_SKINS: Dict[str, List[str]] = list_all_skins()
