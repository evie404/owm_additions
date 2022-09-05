import glob
import os
from typing import Dict, List, Set

if __name__ == "__main__":
    from animation import (
        animation_paths,
        list_all_animations,
        list_all_animations_of_hero,
    )
    from helpers import BASE_PATH
else:
    from owm_additions.paths.animation import (
        animation_paths,
        list_all_animations,
        list_all_animations_of_hero,
    )
    from owm_additions.paths.helpers import BASE_PATH

VICTORY_POSE_ANIMATION_TYPE = "VictoryPose"


def list_all_victory_poses_of_hero(
    hero: str, base_path: str = BASE_PATH
) -> Dict[str, List[str]]:
    return list_all_animations_of_hero(hero, VICTORY_POSE_ANIMATION_TYPE, base_path)


def list_all_victory_poses(base_path: str = BASE_PATH) -> Dict[str, List[str]]:
    return list_all_animations(VICTORY_POSE_ANIMATION_TYPE, base_path)


def victory_pose_animation_paths(
    hero: str, victory_pose_name: str, base_path: str = BASE_PATH
) -> List[str]:
    return animation_paths(
        hero, VICTORY_POSE_ANIMATION_TYPE, victory_pose_name, base_path
    )


def main() -> None:
    # print(list_all_victory_poses())
    print(victory_pose_animation_paths("Mercy", "Toast"))
    # print(list_all_victory_poses())


if __name__ == "__main__":
    main()
