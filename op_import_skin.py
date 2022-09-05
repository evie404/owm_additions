from typing import List, Set

import bpy
from bpy.types import Context

from owm_additions.hero_skins_prop import get_context_hero_name, get_context_skin_name
from owm_additions.paths.skin import entity_paths


class OWM_ADD_ImportSkin(bpy.types.Operator):
    bl_idname = "owm_add.import_skin"
    bl_label = "Import Skin"
    # bl_description = "Clear all bones and object transformations"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        hero = get_context_hero_name(context)
        skin = get_context_skin_name(context)

        import_skin(hero, skin)

        self.report({"INFO"}, f"Finished import {hero} ({skin}).")

        return {"FINISHED"}


def import_skin(hero: str, skin: str) -> None:
    skin_paths: List[str] = entity_paths(hero, skin)

    for skin_path in skin_paths:
        bpy.ops.import_mesh.overtools_entity(filepath=skin_path)
