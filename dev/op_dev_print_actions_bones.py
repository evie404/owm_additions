from typing import Dict, List, Optional, Set, Union

import bpy
from bpy.types import Action, Bone, Context, EditBone, FCurve, PoseBone

from .op_dev_print_selected_bones import str_set_to_dict


class OWM_ADD_Dev_Print_Actions_Bones(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_actions_bones"
    bl_label = "Print Bones used in Actions (Dict)"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context):
        print(str_set_to_dict(find_action_bones(bpy.data.actions)))

        return {"FINISHED"}


class OWM_ADD_Dev_Print_Actions_Bones_Set(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_actions_bones"
    bl_label = "Print Bones used in Actions (Set)"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context):
        print(find_action_bones(bpy.data.actions))

        return {"FINISHED"}


def find_action_bones(actions: List[Action]) -> Set[str]:
    bone_names: Set[str] = set()

    for action in actions:
        for fcurve in action.fcurves:
            fcurve: FCurve

            bone_names.add(fcurve.group.name)

    return bone_names
