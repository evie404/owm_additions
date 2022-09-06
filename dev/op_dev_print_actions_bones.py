from typing import Dict, List, Optional, Set, Union

import bpy
from bpy.types import Action, Bone, Context, EditBone, FCurve, PoseBone

from .op_dev_print_selected_bones import str_set_to_dict


class OWM_ADD_Dev_Print_Actions_Bones(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_actions_bones"
    bl_label = "Print Bones used in Actions (Dict)"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context):
        bone_names: Set[str] = set()

        for action in bpy.data.actions:
            action: Action
            for fcurve in action.fcurves:
                fcurve: FCurve

                bone_names.add(fcurve.group.name)

        print(str_set_to_dict(bone_names))

        return {"FINISHED"}
