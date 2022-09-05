import glob
import os
from typing import List, Set

import bpy
from bpy.types import Context

from ..hero_skins_prop import get_context_hero_name


class OWM_ADD_DevImportAllSkins(bpy.types.Operator):
    bl_idname = "owm_add.import_all_skins"
    bl_label = "Import All Skins"
    # bl_description = "Clear all bones and object transformations"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        hero = get_context_hero_name(context)

        import_all_skins(hero)

        self.report({"INFO"}, f"Finished importing all skins of {hero}.")

        return {"FINISHED"}


def import_all_skins(hero: str) -> None:
    skin_search_path = os.path.join(
        "D:",
        os.sep,
        "Game Extracts",
        "Overwatch",
        "Heroes",
        hero,
        "Skin",
        "*",
        "*",
        "Entities",
        "HeroGallery",
        "HeroGallery.owentity",
    )

    # print(f"skin_search_path: {skin_search_path}")

    skin_paths: List[str] = glob.glob(skin_search_path)

    skin_search_path = os.path.join(
        "D:",
        os.sep,
        "Game Extracts",
        "Overwatch",
        "Heroes",
        hero,
        "Skin",
        "*",
        "*",
        "*",
        "Entities",
        "HeroGallery",
        "HeroGallery.owentity",
    )

    # print(f"skin_search_path: {skin_search_path}")

    skin_paths += glob.glob(skin_search_path)

    # print(skin_paths)

    for skin_path in skin_paths:
        bpy.ops.import_mesh.overtools_entity(
            filepath=skin_path,
            importNormals=False,
            importColor=False,
            importEmpties=False,
            # importMaterial=False,
            import_children=False,
        )
