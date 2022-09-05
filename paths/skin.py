import glob
import os
from typing import Dict, List, Set

from .helpers import BASE_PATH, list_all_heroes, path_element_before, sanitize_name


def list_all_skins_of_hero(hero: str, base_path: str = BASE_PATH) -> List[str]:
    skins: Set[str] = set()
    skins_list: List[str] = []

    skin_paths: List[str] = entity_paths(hero, "*", base_path)

    for skin_path in skin_paths:
        skins.add(path_element_before(skin_path, "Entities"))

    skins_list = list(skins)
    skins_list.sort()

    return skins_list


def list_all_skins(base_path: str = BASE_PATH) -> Dict[str, List[str]]:
    all_skins: Dict[str, List[str]] = {}

    heroes = list_all_heroes(base_path)
    heroes.sort()

    for hero in heroes:
        skins = list_all_skins_of_hero(hero, base_path)

        all_skins[hero] = skins

    return all_skins


def entity_paths(hero: str, skin: str, base_path: str = BASE_PATH) -> List[str]:
    entity_paths: List[str] = []

    for skin_search_path in skin_search_paths(hero, skin, base_path):
        entity_paths += glob.glob(skin_search_path)

    return entity_paths


def skin_search_path(
    hero: str,
    skin: str,
    has_rarity: bool = True,
    base_path: str = BASE_PATH,
) -> str:
    hero_path = sanitize_name(hero)
    skin_path = sanitize_name(skin)

    return os.path.join(
        base_path,
        "Heroes",
        hero_path,
        "Skin",
        *(("*", "*") if has_rarity else ("*")),
        skin_path,
        "Entities",
        "HeroGallery",
        "HeroGallery.owentity",
    )


def skin_search_paths(
    hero: str,
    skin: str,
    base_path: str = BASE_PATH,
) -> List[str]:
    return [
        skin_search_path(hero, skin, has_rarity=False, base_path=base_path),
        skin_search_path(hero, skin, has_rarity=True, base_path=base_path),
    ]


def main() -> None:
    print(list_all_skins())
    # print(entity_paths("Mercy", "*"))
    # print(list_all_victory_poses())


if __name__ == "__main__":
    main()
