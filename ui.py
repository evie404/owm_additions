import bpy
from bpy.types import Context

from .operator import OWM_ADD_UpdateArmature


class OWM_ADD_PT_UpdateArmatureUI(bpy.types.Panel):
    bl_category = "OWM Additions"
    bl_label = "Armature Tools"
    bl_idname = "OWM_ADD_PT_UpdateArmatureUI"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    # @classmethod
    # def poll(cls, context: Context) -> bool:
    #     if "owm.skeleton.model" in bpy.context.active_object.keys():
    #         return True

    #     if "owm.skeleton.name" in bpy.context.active_object.keys():
    #         return True

    #     return False

    def draw(self, context: Context) -> None:
        col = self.layout.column()
        col.operator(
            OWM_ADD_UpdateArmature.bl_idname,
            icon="ARMATURE_DATA",  # text="Landscape"
        )


# bpy.utils.register_class(OWN_ADD_BasePanel)
# bpy.utils.register_class(OWM_ADD_PT_UpdateArmatureUI)