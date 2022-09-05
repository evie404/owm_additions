from typing import List, Set

import bpy
from bpy.types import Armature, Context, Object


class OWM_ADD_Dev_Show_All_Bones(bpy.types.Operator):
    bl_idname = "owm_add.dev_show_all_bones"
    bl_label = "Show All Bones"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context) -> Set[str]:
        arm_objs = all_armature_objects()

        show_all_bones(context, arm_objs)

        return {"FINISHED"}


def show_all_bones(context: Context, arm_objs: List[Object]) -> None:
    for obj in arm_objs:
        context.view_layer.objects.active = obj

        armature: Armature = obj.data

        for i in range(len(armature.layers)):
            armature.layers[i] = True

        bpy.ops.object.mode_set(mode="POSE")

        bpy.ops.pose.select_all(action="DESELECT")

        bpy.ops.pose.reveal()
        bpy.ops.pose.reveal()

        bpy.ops.pose.select_all(action="DESELECT")

        bpy.ops.object.mode_set(mode="OBJECT")


def all_armature_objects() -> List[Object]:
    arm_objs: List[Object] = []

    for obj in bpy.data.objects:
        obj: Object

        if obj.type != "ARMATURE":
            continue

        arm_objs.append(obj)

    return arm_objs
