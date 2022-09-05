from typing import List, Optional, Set

import bpy
from bpy.types import Context, LayerCollection

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

        collection_name = f"{hero} ({skin})"

        if (
            len(context.collection.children) > 0
            or len(context.collection.all_objects) > 0
            or context.collection.name == "Scene Collection"
        ):
            collection = bpy.data.collections.new(collection_name)
            context.collection.children.link(collection)

            layer_collection = find_layer_collection(
                context.view_layer.layer_collection, collection.name
            )
            context.view_layer.active_layer_collection = layer_collection
        else:
            context.collection.name = collection_name

        import_skin(hero, skin)

        self.report({"INFO"}, f"Finished import {hero} ({skin}).")

        return {"FINISHED"}


def find_layer_collection(
    root: LayerCollection, collection_name: str
) -> Optional[LayerCollection]:
    found: Optional[LayerCollection] = None

    if root.name == collection_name:
        return root

    for layer in root.children:
        found = find_layer_collection(layer, collection_name)
        if found:
            return found


def import_skin(hero: str, skin: str) -> None:
    skin_paths: List[str] = entity_paths(hero, skin)

    for skin_path in skin_paths:
        bpy.ops.import_mesh.overtools_entity(filepath=skin_path)
