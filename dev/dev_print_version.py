from typing import Set

import bpy
from bpy.types import Context


class OWM_ADD_PrintVersion(bpy.types.Operator):
    bl_idname = "owm_add.print_version"
    bl_label = "Print Version"
    # bl_description = "Clear all bones and object transformations"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        version = "123"

        self.report({"INFO"}, f"Version: {version}")

        return {"FINISHED"}
