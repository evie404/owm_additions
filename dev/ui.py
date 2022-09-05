import bpy
from bpy.types import Context, UILayout

from .op_dev_allow_select_armatures_only import OWM_ADD_Dev_Allow_Select_Armatures_Only
from .op_dev_find_common_bones import (
    OWM_ADD_DevFindCommonBones,
    OWM_ADD_DevFindFrequentBones,
)
from .op_dev_hide_all_bones_except import OWM_ADD_Dev_Hide_All_Bones_Except
from .op_dev_hide_all_empties import OWM_ADD_Dev_Hide_All_Empties
from .op_dev_import_all_skins import OWM_ADD_DevImportAllSkins
from .op_dev_print_selected_bones import (
    OWM_ADD_Dev_Print_Selected_Bones_Dict,
    OWM_ADD_Dev_Print_Selected_Bones_List,
    OWM_ADD_Dev_Print_Selected_Bones_Set,
)
from .op_dev_print_version import OWM_ADD_PrintVersion


class OWM_ADD_PT_DevPanel(bpy.types.Panel):
    bl_category = "OWM Additions"
    bl_label = "Dev Only"
    bl_idname = "OWM_ADD_PT_DevPanel"
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

        col.operator(
            OWM_ADD_DevFindCommonBones.bl_idname,
            icon="BONE_DATA",
        )

        col.prop(
            context.scene.owm_additions_dev_props,
            "bone_frequency_threshold",
            text="Frequency Threshold",
        )

        col.operator(
            OWM_ADD_DevFindFrequentBones.bl_idname,
            icon="BONE_DATA",
        )

        col.separator()

        col.operator(OWM_ADD_Dev_Hide_All_Empties.bl_idname, icon="EMPTY_DATA")

        col.operator(
            OWM_ADD_Dev_Allow_Select_Armatures_Only.bl_idname, icon="RESTRICT_SELECT_ON"
        )

        if context.object and context.object.pose:
            col.prop_search(
                context.scene.owm_additions_dev_props,
                "bone_to_show",
                context.object.pose,
                "bones",
                text="Bone to Show",
            )
        else:
            col.prop(
                context.scene.owm_additions_dev_props,
                "bone_to_show",
                text="Bone to Show",
            )

        col.operator(OWM_ADD_Dev_Hide_All_Bones_Except.bl_idname, icon="BONE_DATA")

        col.separator()

        col.operator(OWM_ADD_DevImportAllSkins.bl_idname, icon="IMPORT")

        col.separator()

        col.operator(
            OWM_ADD_PrintVersion.bl_idname,
            icon="CONSOLE",
        )

        col.operator("script.reload", icon="FILE_REFRESH")


# bpy.utils.register_class(OWN_ADD_BasePanel)
# bpy.utils.register_class(OWM_ADD_PT_ImportPanel)
