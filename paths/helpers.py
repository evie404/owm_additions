import glob
import os
from pathlib import Path
from typing import List

BASE_PATH = os.path.join(
    "D:",
    os.sep,
    "Game Extracts",
    "Overwatch",
)


def list_all_heroes(base_path: str = BASE_PATH) -> List[str]:
    search_pattern = os.path.join(base_path, "Heroes", "*")

    return [path.split(os.sep)[-1] for path in glob.glob(search_pattern)]


def path_element_before(full_path: str, el: str) -> str:
    parts = Path(full_path).parts
    return parts[parts.index(el) - 1]


def unsanitize_name(name: str) -> str:
    return name.replace("_ 76", ": 76").replace("_ 1776", ": 1776")


def sanitize_name(name: str) -> str:
    return name.replace(": 76", "_ 76").replace(": 1776", "_ 1776")


def main() -> None:
    pass
    # print(list_all_skins())
    # print(entity_paths("Mercy", "*"))
    # print(list_all_victory_poses())


if __name__ == "__main__":
    main()
