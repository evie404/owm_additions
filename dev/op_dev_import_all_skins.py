import glob
import math
import os
from typing import List, Set

import bpy
from bpy.types import Context, Object

from ..importing.asset_prop import get_context_hero_name
from ..organize.collection import (
    hero_skin_collection_name,
    new_child_collection,
    rename_or_new_child_collection,
)
from ..organize.op_organize_hero_objs import find_root, ow_organize_character_objects
from ..paths.skin import entity_paths, list_all_skins_of_hero


class OWM_ADD_DevImportAllSkins(bpy.types.Operator):
    bl_idname = "owm_add.import_all_skins"
    bl_label = "Import All Skins"
    # bl_description = "Clear all bones and object transformations"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        hero = get_context_hero_name(context)

        import_all_skins(context, hero)

        self.report({"INFO"}, f"Finished importing all skins of {hero}.")

        return {"FINISHED"}


def import_all_skins(context: Context, hero: str) -> None:
    skins = list_all_skins_of_hero(hero)

    rename_or_new_child_collection(
        context, hero_skin_collection_name(hero, "All Skins")
    )

    orig_layer_collection = context.view_layer.active_layer_collection

    root_objs: List[Object] = []

    for skin in skins:
        skin_paths: List[str] = entity_paths(hero, skin)
        skin_path = skin_paths[0]

        context.view_layer.active_layer_collection = orig_layer_collection
        new_child_collection(context, hero_skin_collection_name(hero, skin))

        bpy.ops.import_mesh.overtools_entity(
            filepath=skin_path,
            importNormals=False,
            importColor=False,
            importEmpties=False,
            # importMaterial=False,
            import_children=False,
        )

        root_obj = find_root(context)

        ow_organize_character_objects(
            collection=context.collection,
            root_object=root_obj,
            hero=hero,
            skin=skin,
        )

        root_objs.append(root_obj)

    stagger_objects(root_objs)


def stagger_objects(arm_objs: List[Object], spacing: int = 2) -> None:
    divisor = int(math.ceil(math.sqrt(len(arm_objs))))

    for i, obj in enumerate(arm_objs):
        obj.location.x = (i % divisor) * spacing  # - divisor * spacing
        obj.location.y = (i // divisor) * spacing  # - divisor * spacing
