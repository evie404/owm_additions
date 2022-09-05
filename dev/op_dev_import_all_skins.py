import glob
import os
from typing import List, Set

import bpy
from bpy.types import Context

from ..importing.asset_prop import get_context_hero_name
from ..paths.skin import entity_paths


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
    skin_paths: List[str] = entity_paths(hero, "*")

    for skin_path in skin_paths:
        bpy.ops.import_mesh.overtools_entity(
            filepath=skin_path,
            importNormals=False,
            importColor=False,
            importEmpties=False,
            # importMaterial=False,
            import_children=False,
        )
