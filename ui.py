import bpy
from bpy.types import Context

from .bones.dev_hide_all_bones_except import OWM_ADD_Dev_Hide_All_Bones_Except
from .bones.dev_print_selected_bones import (
    OWM_ADD_Dev_Print_Selected_Bones_Dict,
    OWM_ADD_Dev_Print_Selected_Bones_List,
    OWM_ADD_Dev_Print_Selected_Bones_Set,
)
from .bones.operator import OWM_ADD_UpdateArmature
from .dev.dev_allow_select_armatures_only import OWM_ADD_Dev_Allow_Select_Armatures_Only
from .dev.dev_hide_all_empties import OWM_ADD_Dev_Hide_All_Empties
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


class OWM_ADD_DevPanelUI(bpy.types.Panel):
    bl_category = "OWM Additions"
    bl_label = "Dev Only"
    bl_idname = "OWM_ADD_DevPanelUI"
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

        col.operator(
            OWM_ADD_Dev_Print_Selected_Bones_Dict.bl_idname,
            icon="CONSOLE",
        )

        col.operator(
            OWM_ADD_Dev_Print_Selected_Bones_List.bl_idname,
            icon="CONSOLE",
        )

        col.operator(
            OWM_ADD_Dev_Print_Selected_Bones_Set.bl_idname,
            icon="CONSOLE",
        )

        col.operator(OWM_ADD_Dev_Hide_All_Empties.bl_idname, icon="EMPTY_DATA")

        col.operator(
            OWM_ADD_Dev_Allow_Select_Armatures_Only.bl_idname, icon="RESTRICT_SELECT_ON"
        )

        col.prop_search(
            context.scene.owm_additions_dev_props,
            "bone_to_show",
            context.object.pose,
            "bones",
            text="Bone to Show",
        )

        col.operator(OWM_ADD_Dev_Hide_All_Bones_Except.bl_idname, icon="BONE_DATA")


# bpy.utils.register_class(OWN_ADD_BasePanel)
# bpy.utils.register_class(OWM_ADD_PanelUI)
