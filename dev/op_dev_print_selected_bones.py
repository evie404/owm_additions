from typing import Dict, Set

import bpy
from bpy.types import Context


class OWM_ADD_Dev_Print_Selected_Bones_List(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_selected_bones_list"
    bl_label = "Print Selected Bones (List)"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context):
        if not context.active_object:
            self.report({"ERROR_INVALID_CONTEXT"}, "Please select a OWM armature.")
            return {"CANCELLED"}

        obj = context.active_object

        if not (obj and obj.type == "ARMATURE"):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected object is not an armature."
            )

            return {"CANCELLED"}

        print(list(selected_bones_set(context)))

        return {"FINISHED"}


class OWM_ADD_Dev_Print_Selected_Bones_Set(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_selected_bones_set"
    bl_label = "Print Selected Bones (Set)"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context):
        if not context.active_object:
            self.report({"ERROR_INVALID_CONTEXT"}, "Please select a OWM armature.")
            return {"CANCELLED"}

        obj = context.active_object

        if not (obj and obj.type == "ARMATURE"):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected object is not an armature."
            )

            return {"CANCELLED"}

        print(selected_bones_set(context))

        return {"FINISHED"}


class OWM_ADD_Dev_Print_Selected_Bones_Dict(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_selected_bones_dict"
    bl_label = "Print Selected Bones (Dict)"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context):
        if not context.active_object:
            self.report({"ERROR_INVALID_CONTEXT"}, "Please select a OWM armature.")
            return {"CANCELLED"}

        obj = context.active_object

        if not (obj and obj.type == "ARMATURE"):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected object is not an armature."
            )

            return {"CANCELLED"}

        print(selected_bones_dict(context))

        return {"FINISHED"}


def selected_bones_set(context: Context) -> Set[str]:
    selected_bones: Set[str] = set()

    if context.selected_bones:
        for bone in context.selected_bones:
            selected_bones.add(bone.name)

    if context.selected_pose_bones:
        for bone in context.selected_pose_bones:
            selected_bones.add(bone.name)

    if context.selected_editable_bones:
        for bone in context.selected_editable_bones:
            selected_bones.add(bone.name)

    return selected_bones


def selected_bones_dict(context: Context) -> Dict[str, str]:
    return str_set_to_dict(selected_bones_set(context))


def str_set_to_dict(s: Set[str]) -> Dict[str, str]:
    d: Dict[str, str] = {}

    for el in s:
        d[el] = ""

    return d
