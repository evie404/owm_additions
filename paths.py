import glob
import os
from typing import List


def unsanitize_name(name: str) -> str:
    return name.replace("_ 76", ": 76").replace("_ 1776", ": 1776")


def sanitize_name(name: str) -> str:
    return name.replace(": 76", "_ 76").replace(": 1776", "_ 1776")


def entity_paths(hero: str, skin: str) -> List[str]:
    entity_paths: List[str] = []

    for skin_search_path in skin_search_paths(hero, skin):
        entity_paths += glob.glob(skin_search_path)

    return entity_paths


def skin_search_paths(hero: str, skin: str) -> List[str]:
    hero_path = sanitize_name(hero)
    skin_path = sanitize_name(skin)

    return [
        os.path.join(
            "D:",
            os.sep,
            "Game Extracts",
            "Overwatch",
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
            "D:",
            os.sep,
            "Game Extracts",
            "Overwatch",
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
