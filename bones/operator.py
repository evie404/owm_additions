import bpy
from bpy.types import Context
from owm_additions.bones.update_bones import update_bones
from owm_additions.hero_skins_prop import get_context_hero_name, get_context_skin_name


class OWM_ADD_UpdateArmature(bpy.types.Operator):
    bl_idname = "owm_add.update_armature"
    bl_label = "Update Armature"
    # bl_description = "Clear all bones and object transformations"
    bl_options = {"UNDO"}

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

        hero = get_context_hero_name(context)
        skin = get_context_skin_name(context)

        update_bones(character=hero, skin=skin)

        self.report({"INFO"}, f"Finished updating armature with {hero} ({skin}).")

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context) -> bool:
        return (
            context.mode == "OBJECT"
            and context.active_object
            and context.active_object.type == "ARMATURE"
            and "owm.skeleton.model" in context.active_object.keys()
            and "owm.skeleton.name" in context.active_object.keys()
        )
