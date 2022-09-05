import glob
import os
from typing import Dict, List

BASE_PATH = os.path.join(
    "D:",
    os.sep,
    "Game Extracts",
    "Overwatch",
)


def list_all_heroes(base_path: str = BASE_PATH) -> List[str]:
    search_pattern = os.path.join(base_path, "Heroes", "*")

    return [path.split(os.sep)[-1] for path in glob.glob(search_pattern)]


def list_all_skins_of_hero(hero: str, base_path: str = BASE_PATH) -> List[str]:
    skins: List[str] = []

    prefix = os.path.join(base_path, "Heroes", hero, "Skin") + os.sep
    suffix = os.sep + os.path.join(
        "Entities",
        "HeroGallery",
        "HeroGallery.owentity",
    )

    no_rarity_paths: List[str] = glob.glob(f"{prefix}*{os.sep}*{suffix}")

    skins = [
        skin.replace(prefix, "").replace(suffix, "").split(os.sep)[-1]
        for skin in no_rarity_paths
    ]

    rarity_paths: List[str] = glob.glob(f"{prefix}*{os.sep}*{os.sep}*{suffix}")

    skins += [
        skin.replace(prefix, "").replace(suffix, "").split(os.sep)[-1]
        for skin in rarity_paths
    ]

    skins.sort()

    return skins


def list_all_skins(base_path: str = BASE_PATH) -> Dict[str, List[str]]:
    all_skins: Dict[str, List[str]] = {}

    heroes = list_all_heroes(base_path)
    heroes.sort()

    for hero in heroes:
        skins = list_all_skins_of_hero(hero, base_path)

        all_skins[hero] = skins

    return all_skins


def unsanitize_name(name: str) -> str:
    return name.replace("_ 76", ": 76").replace("_ 1776", ": 1776")


def sanitize_name(name: str) -> str:
    return name.replace(": 76", "_ 76").replace(": 1776", "_ 1776")


def entity_paths(hero: str, skin: str) -> List[str]:
    entity_paths: List[str] = []

    for skin_search_path in skin_search_paths(hero, skin):
        entity_paths += glob.glob(skin_search_path)

    return entity_paths


def skin_search_paths(
    hero: str,
    skin: str,
    base_path: str = BASE_PATH,
) -> List[str]:
    hero_path = sanitize_name(hero)
    skin_path = sanitize_name(skin)

    return [
        os.path.join(
            base_path,
            "Heroes",
            hero_path,
            "Skin",
            "*",
            skin_path,
            "Entities",
            "HeroGallery",
            "HeroGallery.owentity",
        ),
        os.path.join(
            base_path,
            "Heroes",
            hero_path,
            "Skin",
            "*",
            "*",
            skin_path,
            "Entities",
            "HeroGallery",
            "HeroGallery.owentity",
        ),
    ]
