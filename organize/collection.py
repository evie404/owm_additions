from typing import Optional

import bpy
from bpy.types import Context, LayerCollection


def hero_skin_collection_name(hero: str, skin: str) -> str:
    return f"{hero} ({skin})"


def rename_or_new_child_collection(context: Context, collection_name: str) -> None:
    if (
        len(context.collection.children) > 0
        or len(context.collection.all_objects) > 0
        or context.collection.name == "Scene Collection"
    ):
        new_child_collection(context, collection_name)
    else:
        context.collection.name = collection_name


def new_child_collection(context: Context, collection_name: str) -> None:
    collection = bpy.data.collections.new(collection_name)
    context.collection.children.link(collection)

    layer_collection = find_layer_collection(
        context.view_layer.layer_collection, collection.name
    )
    context.view_layer.active_layer_collection = layer_collection


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
