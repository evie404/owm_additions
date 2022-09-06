import bpy
from bpy.types import Context, UILayout

from ..importing.assets import HERO_SKINS
from .op_dev_allow_select_armatures_only import OWM_ADD_Dev_Allow_Select_Armatures_Only
from .op_dev_apply_base_mapping_to_all import OWM_ADD_Dev_Apply_Base_Mapping_To_All
from .op_dev_find_common_bones import (
    OWM_ADD_DevFindCommonBones,
    OWM_ADD_DevFindFrequentBones,
)
from .op_dev_hide_all_empties import OWM_ADD_Dev_Hide_All_Empties
from .op_dev_import_all_skins import OWM_ADD_DevImportAllSkins
from .op_dev_print_actions_bones import (
    OWM_ADD_Dev_Print_Actions_Bones,
    OWM_ADD_Dev_Print_Actions_Bones_Set,
)
from .op_dev_print_bone_children import OWM_ADD_Dev_Print_Bone_Children_Dict
from .op_dev_print_selected_bones import (
    OWM_ADD_Dev_Print_Selected_Bones_Dict,
    OWM_ADD_Dev_Print_Selected_Bones_List,
    OWM_ADD_Dev_Print_Selected_Bones_Set,
)
from .op_dev_print_version import OWM_ADD_PrintVersion
from .op_dev_show_hide_bones import (
    OWM_ADD_Dev_Hide_All_Bones_Except,
    OWM_ADD_Dev_Show_All_Bones,
    OWM_ADD_Dev_Show_Only_Unknown_Bones,
)


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
            OWM_ADD_Dev_Print_Bone_Children_Dict.bl_idname,
            icon="CONSOLE",
        )

        col.operator(
            OWM_ADD_Dev_Print_Actions_Bones.bl_idname,
            icon="CONSOLE",
        )

        col.operator(
            OWM_ADD_Dev_Print_Actions_Bones_Set.bl_idname,
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

        col.operator(OWM_ADD_Dev_Show_All_Bones.bl_idname, icon="BONE_DATA")
        col.operator(OWM_ADD_Dev_Show_Only_Unknown_Bones.bl_idname, icon="BONE_DATA")

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

        self._draw_hero_search(col, context)
        col.operator(OWM_ADD_DevImportAllSkins.bl_idname, icon="IMPORT")
        col.operator(
            OWM_ADD_Dev_Apply_Base_Mapping_To_All.bl_idname, icon="ARMATURE_DATA"
        )

        col.separator()

        col.operator(
            OWM_ADD_PrintVersion.bl_idname,
            icon="CONSOLE",
        )

        col.operator("script.reload", icon="FILE_REFRESH")

    # TODO: reuse
    def _draw_hero_search(self, col: UILayout, context: Context) -> None:
        id_store = bpy.context.window_manager
        owm_additions_hero_options = id_store.owm_additions_hero_options

        owm_additions_hero_options.clear()

        for name in sorted(HERO_SKINS.keys()):
            item = owm_additions_hero_options.add()
            item.name = name

        col.prop_search(
            context.scene.owm_additions_import_assets,
            "hero",
            id_store,
            "owm_additions_hero_options",
            text="Hero",
        )
