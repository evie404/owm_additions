import bpy
from bpy.types import Context, UILayout

from ..bones.dev_find_common_bones import (OWM_ADD_DevFindCommonBones,
                                           OWM_ADD_DevFindFrequentBones)
from ..bones.dev_hide_all_bones_except import OWM_ADD_Dev_Hide_All_Bones_Except
from ..bones.dev_print_selected_bones import (
    OWM_ADD_Dev_Print_Selected_Bones_Dict,
    OWM_ADD_Dev_Print_Selected_Bones_List,
    OWM_ADD_Dev_Print_Selected_Bones_Set)
from ..dev.dev_allow_select_armatures_only import \
    OWM_ADD_Dev_Allow_Select_Armatures_Only
from ..dev.dev_hide_all_empties import OWM_ADD_Dev_Hide_All_Empties
from ..dev.dev_import_all_skins import OWM_ADD_DevImportAllSkins
from ..dev.dev_print_version import OWM_ADD_PrintVersion
from .assets import (HERO_EMOTES, HERO_HIGHLIGHT_INTROS, HERO_SKINS,
                     HERO_VICTORY_POSES)
from .op_import_animations import (OWM_ADD_ImportEmote,
                                   OWM_ADD_ImportHighlightIntro,
                                   OWM_ADD_ImportVictoryPose)
from .op_import_skin import OWM_ADD_ImportSkin


class OWM_ADD_PT_ImportPanel(bpy.types.Panel):
    bl_category = "OWM Additions"
    bl_label = "Import OW Assets"
    bl_idname = "OWM_ADD_PT_ImportPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_context = "objectmode"
    # bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context: Context) -> None:
        col = self.layout.column()

        self._draw_hero_search(col, context)
        self._draw_skin_search(col, context)
        col.operator(OWM_ADD_ImportSkin.bl_idname, icon="IMPORT")

        col.separator()
        self._draw_victory_pose_search(col, context)
        col.operator(OWM_ADD_ImportVictoryPose.bl_idname, icon="IMPORT")

        col.separator()
        self._draw_highlight_intro_search(col, context)
        col.operator(OWM_ADD_ImportHighlightIntro.bl_idname, icon="IMPORT")

        col.separator()
        self._draw_emote_search(col, context)
        col.operator(OWM_ADD_ImportEmote.bl_idname, icon="IMPORT")

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

    def _draw_skin_search(self, col: UILayout, context: Context) -> None:
        id_store = bpy.context.window_manager
        owm_additions_skin_options = id_store.owm_additions_skin_options

        owm_additions_skin_options.clear()

        hero = context.scene.owm_additions_import_assets.hero
        skins = HERO_SKINS.get(hero, [])

        for name in skins:
            item = owm_additions_skin_options.add()
            item.name = name

        col.prop_search(
            context.scene.owm_additions_import_assets,
            "skin",
            id_store,
            "owm_additions_skin_options",
            text="Skin",
        )

    def _draw_victory_pose_search(self, col: UILayout, context: Context) -> None:
        id_store = bpy.context.window_manager
        owm_additions_victory_pose_options = id_store.owm_additions_victory_pose_options

        owm_additions_victory_pose_options.clear()

        hero = context.scene.owm_additions_import_assets.hero
        victory_poses = HERO_VICTORY_POSES.get(hero, [])

        for name in victory_poses:
            item = owm_additions_victory_pose_options.add()
            item.name = name

        col.prop_search(
            context.scene.owm_additions_import_assets,
            "victory_pose",
            id_store,
            "owm_additions_victory_pose_options",
            text="Victory Pose",
        )

    def _draw_highlight_intro_search(self, col: UILayout, context: Context) -> None:
        id_store = bpy.context.window_manager
        owm_additions_highlight_intro_options = (
            id_store.owm_additions_highlight_intro_options
        )

        owm_additions_highlight_intro_options.clear()

        hero = context.scene.owm_additions_import_assets.hero
        highlight_intros = HERO_HIGHLIGHT_INTROS.get(hero, [])

        for name in highlight_intros:
            item = owm_additions_highlight_intro_options.add()
            item.name = name

        col.prop_search(
            context.scene.owm_additions_import_assets,
            "highlight_intro",
            id_store,
            "owm_additions_highlight_intro_options",
            text="Highlight Intro",
        )

    def _draw_emote_search(self, col: UILayout, context: Context) -> None:
        id_store = bpy.context.window_manager
        owm_additions_emote_options = id_store.owm_additions_emote_options

        owm_additions_emote_options.clear()

        hero = context.scene.owm_additions_import_assets.hero
        emotes = HERO_EMOTES.get(hero, [])

        for name in emotes:
            item = owm_additions_emote_options.add()
            item.name = name

        col.prop_search(
            context.scene.owm_additions_import_assets,
            "emote",
            id_store,
            "owm_additions_emote_options",
            text="Emote",
        )


class OWM_ADD_PT_DevPanelUI(bpy.types.Panel):
    bl_category = "OWM Additions"
    bl_label = "Dev Only"
    bl_idname = "OWM_ADD_PT_DevPanelUI"
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