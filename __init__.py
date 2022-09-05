from operator import mod
from typing import List, Type

from .dev.ui import OWM_ADD_PT_DevPanel

reloaded = False

if "bpy" in locals():
    reloaded = True

bl_info = {
    "name": "OWM Additions",
    "author": "SushiKitty",
    "version": (0, 0, 1),
    "blender": (2, 92, 0),
    # "location": "File > Import > OWM",
    "description": "Cleanup OWM exports from TankLib or DataTool",
    "wiki_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Import-Export",
}

import bpy


def reload():
    import importlib
    from sys import modules

    for module in set(modules.values()):
        try:
            if module.__name__.startswith("owm_additions"):
                importlib.reload(module)
        except:
            pass


if reloaded:
    reload()


class OWM_ADD_NameProp(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()


def all_classes() -> List[Type]:
    from .bones.op_update_armature import OWM_ADD_UpdateArmature
    from .dev.op_dev_allow_select_armatures_only import (
        OWM_ADD_Dev_Allow_Select_Armatures_Only,
    )
    from .dev.op_dev_find_common_bones import (
        OWM_ADD_DevFindCommonBones,
        OWM_ADD_DevFindFrequentBones,
    )
    from .dev.op_dev_hide_all_bones_except import OWM_ADD_Dev_Hide_All_Bones_Except
    from .dev.op_dev_hide_all_empties import OWM_ADD_Dev_Hide_All_Empties
    from .dev.op_dev_import_all_skins import OWM_ADD_DevImportAllSkins
    from .dev.op_dev_print_selected_bones import (
        OWM_ADD_Dev_Print_Selected_Bones_Dict,
        OWM_ADD_Dev_Print_Selected_Bones_List,
        OWM_ADD_Dev_Print_Selected_Bones_Set,
    )
    from .dev.op_dev_print_version import OWM_ADD_PrintVersion
    from .dev.op_dev_prop import OWM_ADD_Dev_Props
    from .importing.asset_prop import OWM_Asset_Prop
    from .importing.op_import_animations import (
        OWM_ADD_ImportEmote,
        OWM_ADD_ImportHighlightIntro,
        OWM_ADD_ImportVictoryPose,
    )
    from .importing.op_import_skin import OWM_ADD_ImportSkin
    from .importing.ui import OWM_ADD_PT_ImportPanel
    from .organize.op_organize_hero_objs import OWM_ADD_Organize_Hero_Objects
    from .organize.ui import OWM_ADD_PT_OrganizePanel

    return [
        OWM_ADD_NameProp,
        OWM_Asset_Prop,
        OWM_ADD_Dev_Props,
        OWM_ADD_UpdateArmature,
        OWM_ADD_Organize_Hero_Objects,
        OWM_ADD_ImportSkin,
        OWM_ADD_ImportVictoryPose,
        OWM_ADD_ImportHighlightIntro,
        OWM_ADD_ImportEmote,
        OWM_ADD_DevImportAllSkins,
        OWM_ADD_DevFindCommonBones,
        OWM_ADD_DevFindFrequentBones,
        OWM_ADD_Dev_Allow_Select_Armatures_Only,
        OWM_ADD_Dev_Hide_All_Bones_Except,
        OWM_ADD_Dev_Hide_All_Empties,
        OWM_ADD_Dev_Print_Selected_Bones_Dict,
        OWM_ADD_Dev_Print_Selected_Bones_List,
        OWM_ADD_Dev_Print_Selected_Bones_Set,
        OWM_ADD_PrintVersion,
        OWM_ADD_PT_ImportPanel,
        OWM_ADD_PT_OrganizePanel,
        OWM_ADD_PT_DevPanel,
    ]


def register():
    for cls in all_classes():
        print(f"registering {cls}...")
        bpy.utils.register_class(cls)

    from .dev.op_dev_prop import OWM_ADD_Dev_Props
    from .importing.asset_prop import OWM_Asset_Prop

    bpy.types.Scene.owm_additions_import_assets = bpy.props.PointerProperty(
        type=OWM_Asset_Prop
    )

    bpy.types.Scene.owm_additions_dev_props = bpy.props.PointerProperty(
        type=OWM_ADD_Dev_Props
    )

    IDStore = bpy.types.WindowManager
    IDStore.owm_additions_hero_options = bpy.props.CollectionProperty(
        type=OWM_ADD_NameProp
    )
    IDStore.owm_additions_skin_options = bpy.props.CollectionProperty(
        type=OWM_ADD_NameProp
    )
    IDStore.owm_additions_victory_pose_options = bpy.props.CollectionProperty(
        type=OWM_ADD_NameProp
    )
    IDStore.owm_additions_highlight_intro_options = bpy.props.CollectionProperty(
        type=OWM_ADD_NameProp
    )
    IDStore.owm_additions_emote_options = bpy.props.CollectionProperty(
        type=OWM_ADD_NameProp
    )


def unregister():
    for cls in all_classes():
        print(f"unregistering {cls}...")
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.owm_additions_import_assets
    del bpy.types.Scene.owm_additions_dev_props

    IDStore = bpy.types.WindowManager
    del IDStore.owm_additions_hero_options
    del IDStore.owm_additions_skin_options
    del IDStore.owm_additions_victory_pose_options
    del IDStore.owm_additions_highlight_intro_options
    del IDStore.owm_additions_emote_options


if __name__ == "__main__":
    register()
