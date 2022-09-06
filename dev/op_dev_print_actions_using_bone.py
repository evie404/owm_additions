from typing import Dict, List, Optional, Set, Union

import bpy
from bpy.types import Action, Bone, Context, EditBone, FCurve, PoseBone

from ..importing.asset_prop import get_context_hero_name
from .op_dev_find_common_bones import all_base_bones
from .op_dev_print_selected_bones import str_set_to_dict


class OWM_ADD_Dev_Print_Actions_Using_Bone(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_actions_using_bone"
    bl_label = "Print Actions Using Bone"
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

        bone_name = context.scene.owm_additions_dev_props.bone_to_show
        print(find_actions_using_bone(bone_name))

        return {"FINISHED"}


def find_actions_using_bone(bone: str) -> Set[Action]:
    actions: Set[Action] = set()

    for action in bpy.data.actions:
        action: Action

        using = False

        for fcurve in action.fcurves:
            fcurve: FCurve

            if fcurve.group.name == bone:
                using = True
                break

        if using:
            actions.add(action)

    return actions
