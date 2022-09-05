import bpy
from bpy.props import EnumProperty
from bpy.types import Context

from .update_bones import update_bones


class OWM_ADD_UpdateArmature(bpy.types.Operator):
    bl_idname = "owm_add.update_armature"
    bl_label = "Update Armature"
    # bl_description = "Clear all bones and object transformations"
    bl_options = {"UNDO"}

    character: EnumProperty(
        name="Character",
        # default="",
        # description="Marble bias",
        items=[
            # ("Mercy", "Mercy", "", 0),
            ("Pharah", "Pharah", "", 1),
        ],
    )

    skin: EnumProperty(
        name="Skin",
        # default="",
        # description="Marble bias",
        items=[
            # ("Dr. Ziegler", "Default", "", 0),
            # ("Zhuque", "Zhuque", "", 0),
            ("Qinglong", "Qinglong", "", 0),
            # ("Default", "Default", "", 0),
            # ("Pharah", "Pharah", "", 1),
        ],
    )

    def execute(self, context: Context):
        if not bpy.context.active_object:
            self.report({"ERROR_INVALID_CONTEXT"}, "Please select a OWM armature.")
            return {"CANCELLED"}

        obj = bpy.context.active_object

        if not (obj and obj.type == "ARMATURE"):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected object is not an armature."
            )

            return {"CANCELLED"}

        if (
            "owm.skeleton.model" not in obj.keys()
            and "owm.skeleton.name" not in obj.keys()
        ):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected armature is not an OWM armature."
            )
            return {"CANCELLED"}

        update_bones(character=self.character, skin=self.skin)

        self.report(
            {"INFO"}, f"Finished updating armature with {self.character} ({self.skin})."
        )

        return {"FINISHED"}
