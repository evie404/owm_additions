from typing import Optional

import bpy
from bpy.types import Armature, Context, Object

# from .bones.bone_names import rename_all_bones
from .bone_groups import assign_bone_groups, clear_bone_groups
from .bone_layers import assign_bone_layers, clear_bone_layers
from .bone_names import rename_all_bones


def update_bones(
    context: Context,
    obj: Object,
    character: Optional[str] = None,
    skin: Optional[str] = None,
    rename_bones: bool = False,
) -> None:
    context.view_layer.objects.active = obj
    armature: Armature = obj.data

    for i in range(32):
        armature.layers[i] = True

    bpy.ops.object.mode_set(mode="POSE")
    clear_bone_groups(obj)
    assign_bone_groups(obj, character, skin)

    bpy.ops.object.mode_set(mode="EDIT")
    clear_bone_layers(armature)
    assign_bone_layers(armature, character, skin)

    if rename_bones:
        rename_all_bones(armature, character, skin)

    bpy.ops.object.mode_set(mode="OBJECT")
