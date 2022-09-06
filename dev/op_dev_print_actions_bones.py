from typing import Dict, List, Optional, Set, Union

import bpy
from bpy.types import Action, Bone, Context, EditBone, FCurve, PoseBone

from ..importing.asset_prop import get_context_hero_name
from .op_dev_find_common_bones import all_base_bones
from .op_dev_print_selected_bones import str_set_to_dict


class OWM_ADD_Dev_Print_Actions_Bones(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_actions_bones_dict"
    bl_label = "Print Bones used in Actions (Dict)"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context):
        hero = get_context_hero_name(context)

        action_bones = find_action_bones(bpy.data.actions)

        base_bones = all_base_bones(hero)

        print(f"in action but not in base: {action_bones.difference(base_bones)}")
        print(f"in base but not in action: {base_bones.difference(action_bones)}")

        # print(str_set_to_dict(find_action_bones(bpy.data.actions)))

        return {"FINISHED"}


class OWM_ADD_Dev_Print_Actions_Bones_Set(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_actions_bones_set"
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
