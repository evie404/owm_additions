from typing import Optional

import bpy

# from .bone_names import rename_all_bones
from .bone_groups import assign_bone_groups, clear_bone_groups
from .bone_layers import assign_bone_layers, clear_bone_layers


def update_bones(character: Optional[str] = None, skin: Optional[str] = None) -> None:
    armobj = bpy.context.active_object

    if not (armobj and armobj.type == "ARMATURE"):
        print("no objects selected or selected object is not an armature.")
        return

    for i in range(32):
        bpy.context.object.data.layers[i] = True

    bpy.ops.object.mode_set(mode="POSE")
    clear_bone_groups(armobj)
    assign_bone_groups(armobj, character, skin)

    bpy.ops.object.mode_set(mode="EDIT")
    clear_bone_layers(armobj.data)
    assign_bone_layers(armobj.data, character, skin)

    # rename_all_bones(armobj.data, character, skin)

    bpy.ops.object.mode_set(mode="OBJECT")


update_bones("Mercy", "Dr. Ziegler")
