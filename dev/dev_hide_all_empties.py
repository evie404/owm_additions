from typing import Set

import bpy
from bpy.types import Context, Object


class OWM_ADD_Dev_Hide_All_Empties(bpy.types.Operator):
    bl_idname = "owm_add.dev_hide_all_empties"
    bl_label = "Hide All Empties"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, _: Context) -> Set[str]:
        for obj in bpy.data.objects:
            obj: Object

            if obj.type != "EMPTY":
                continue

            obj.hide_set(True)

        return {"FINISHED"}
