from typing import Set

import bpy
from bpy.types import Context, Object


class OWM_ADD_Dev_Allow_Select_Armatures_Only(bpy.types.Operator):
    bl_idname = "owm_add.dev_allow_select_armatures_only"
    bl_label = "Allow Select Armatures Only"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, _: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object

            if obj.type == "ARMATURE":
                continue

            obj.hide_select = True

        return {"FINISHED"}
