import glob
import os
from pathlib import Path
from typing import Dict, List, Set

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
    skins: Set[str] = set()
    skins_list: List[str] = []

    skin_paths: List[str] = entity_paths(hero, "*", base_path)

    for skin_path in skin_paths:
        skins.add(path_element_before(skin_path, "Entities"))

    skins_list = list(skins)
    skins_list.sort()

    return skins_list


def path_element_before(full_path: str, el: str) -> str:
    parts = Path(full_path).parts
    return parts[parts.index(el) - 1]


def list_all_victory_poses_of_hero(
    hero: str, base_path: str = BASE_PATH
) -> Dict[str, List[str]]:
    victory_poses: Set[str] = set()
    victory_poses_list: List[str] = []

    victory_pose_paths: List[str] = glob.glob(
        victory_pose_animations_search_path(hero, "*", base_path)
    )

    for victory_pose_path in victory_pose_paths:
        victory_poses.add(path_element_before(victory_pose_path, "Animations"))

    victory_poses_list = list(victory_poses)
    victory_poses_list.sort()

    return victory_poses_list


def list_all_victory_poses(base_path: str = BASE_PATH) -> Dict[str, List[str]]:
    all_victory_poses: Dict[str, List[str]] = {}

    heroes = list_all_heroes(base_path)
    heroes.sort()

    for hero in heroes:
        victory_poses = list_all_victory_poses_of_hero(hero, base_path)

        all_victory_poses[hero] = victory_poses

    return all_victory_poses


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


def entity_paths(hero: str, skin: str, base_path: str = BASE_PATH) -> List[str]:
    entity_paths: List[str] = []

    for skin_search_path in skin_search_paths(hero, skin, base_path):
        entity_paths += glob.glob(skin_search_path)

    return entity_paths


def victory_pose_search_path(
    hero: str,
    victory_pose: str,
    base_path: str = BASE_PATH,
) -> str:
    return os.path.join(
        base_path, "Heroes", sanitize_name(hero), "VictoryPose", "*", "*", victory_pose
    )


def victory_pose_animations_search_path(
    hero: str,
    victory_pose: str,
    base_path: str = BASE_PATH,
) -> str:
    return os.path.join(
        victory_pose_search_path(hero, victory_pose, base_path),
        "Animations",
        "*",  # priority
        "*.seanim",
    )


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
