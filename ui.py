import bpy
from bpy.types import Context

from .bones.operator import OWM_ADD_UpdateArmature
from .organize_hero_objs import OWM_ADD_Organize_Hero_Objects


class OWM_ADD_PanelUI(bpy.types.Panel):
    bl_category = "OWM Additions"
    bl_label = "Update OWM Imports"
    bl_idname = "OWM_ADD_PanelUI"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_context = "objectmode"
    # bl_options = {"DEFAULT_CLOSED"}

    # @classmethod
    # def poll(cls, context: Context) -> bool:
    #     if "owm.skeleton.model" in bpy.context.active_object.keys():
    #         return True

    #     if "owm.skeleton.name" in bpy.context.active_object.keys():
    #         return True

    #     return False

    def draw(self, context: Context) -> None:
        col = self.layout.column()

        col.prop(
            context.scene.owm_additions_hero_skin,
            "hero",
            text="Hero",
        )

        col.prop(context.scene.owm_additions_hero_skin, "skin", text="Skin")

        col.operator(
            OWM_ADD_UpdateArmature.bl_idname,
            icon="ARMATURE_DATA",  # text="Landscape"
        )

        col.operator(
            OWM_ADD_Organize_Hero_Objects.bl_idname,
            icon="OUTLINER_COLLECTION",
        )


# bpy.utils.register_class(OWN_ADD_BasePanel)
# bpy.utils.register_class(OWM_ADD_PanelUI)
