from typing import Dict, List

from .paths import list_all_skins

HERO_SKINS: Dict[str, List[str]] = list_all_skins()
