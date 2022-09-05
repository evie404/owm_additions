import glob
import os
from typing import Dict, List, Set

if __name__ == "__main__":
    from helpers import BASE_PATH, list_all_heroes, path_element_before, sanitize_name
else:
    from owm_additions.paths.helpers import (
        BASE_PATH,
        list_all_heroes,
        path_element_before,
        sanitize_name,
    )


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


def main() -> None:
    print(list_all_victory_poses())
    # print(entity_paths("Mercy", "*"))
    # print(list_all_victory_poses())


if __name__ == "__main__":
    main()
