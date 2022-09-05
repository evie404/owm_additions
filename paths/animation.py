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

VICTORY_POSE_ANIMATION_TYPE = "VictoryPose"
HIGHLIGHT_INTRO_ANIMATION_TYPE = "HighlightIntro"
EMOTE_ANIMATION_TYPE = "Emote"


def list_all_animations_of_hero(
    hero: str, animation_type: str, base_path: str = BASE_PATH
) -> List[str]:
    animations: Set[str] = set()
    animations_list: List[str] = []

    animation_paths: List[str] = glob.glob(
        animation_files_search_path(hero, animation_type, "*", "*", base_path)
    )

    # print(animation_paths)

    for animation_path in animation_paths:
        animations.add(path_element_before(animation_path, "Animations"))

    animations_list = list(animations)
    animations_list.sort()

    return animations_list


def list_all_animations(
    animation_type: str, base_path: str = BASE_PATH
) -> Dict[str, List[str]]:
    all_animations: Dict[str, List[str]] = {}

    heroes = list_all_heroes(base_path)
    heroes.sort()

    for hero in heroes:
        animations = list_all_animations_of_hero(hero, animation_type, base_path)

        all_animations[hero] = animations

    return all_animations


def animation_paths(
    hero: str,
    animation_type: str,
    animation_name: str,
    base_path: str = BASE_PATH,
) -> List[str]:
    animation_paths: List[str] = []
    animation_dirs_search_path: str = animation_files_search_path(
        hero, animation_type, animation_name, "*", base_path
    )

    animation_paths += glob.glob(animation_dirs_search_path)

    return animation_paths


def animation_paths_by_priority(
    hero: str,
    animation_type: str,
    animation_name: str,
    base_path: str = BASE_PATH,
) -> Dict[int, List[str]]:
    results = glob.glob(
        animation_priorities_search_path(
            hero, animation_type, animation_name, base_path
        )
    )

    priorities: List[int] = []
    animations_by_priority: Dict[int, List[str]] = {}

    for result in results:
        priority = int(os.path.basename(os.path.normpath(result)))
        priorities.append(priority)

    for priority in priorities:
        results = glob.glob(
            animation_files_search_path(
                hero, animation_type, animation_name, str(priority), base_path
            )
        )

        if len(results) > 0:
            animations_by_priority[priority] = results

    return animations_by_priority


def animation_dirs_search_path(
    hero: str,
    animation_type: str,
    animation_name: str,
    base_path: str = BASE_PATH,
) -> str:
    return os.path.join(
        base_path,
        "Heroes",
        sanitize_name(hero),
        animation_type,
        "*",
        "*",
        animation_name,
    )


def animation_priorities_search_path(
    hero: str,
    animation_type: str,
    animation_name: str,
    base_path: str = BASE_PATH,
) -> str:
    return os.path.join(
        animation_dirs_search_path(hero, animation_type, animation_name, base_path),
        "Animations",
        "*",
    )


def animation_files_search_path(
    hero: str,
    animation_type: str,
    animation_name: str,
    priority: str,
    base_path: str = BASE_PATH,
) -> str:
    return os.path.join(
        animation_dirs_search_path(hero, animation_type, animation_name, base_path),
        "Animations",
        priority,
        "*.seanim",
    )


def main() -> None:
    # print(list_all_animations())
    # print(animation_paths("Mercy", EMOTE_ANIMATION_TYPE, "*"))
    # print(animation_paths_by_priority("Ana", EMOTE_ANIMATION_TYPE, "Heroic"))
    # print(list_all_animations())
    print(list_all_animations_of_hero("Ana", EMOTE_ANIMATION_TYPE))


if __name__ == "__main__":
    main()
