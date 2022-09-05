from typing import List, Type

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


class OWM_ADD_NameProp(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty()


# Script reloading (if the user calls 'Reload Scripts' from Blender)
# https://github.com/KhronosGroup/glTF-Blender-IO/blob/04e26bef903543d08947c5a9a5fea4e787b68f17/addons/io_scene_gltf2/__init__.py#L32-L54
# http://www.apache.org/licenses/LICENSE-2.0
def reload_package(module_dict_main: dict) -> None:  # type: ignore[type-arg]
    # Lazy import to minimize initialization before reload_package()
    import importlib
    from pathlib import Path
    from typing import Any, Dict

    def reload_package_recursive(
        current_dir: Path, module_dict: Dict[str, Any]
    ) -> None:
        for path in current_dir.iterdir():
            if "__init__" in str(path) or path.stem not in module_dict:
                continue

            if path.is_file() and path.suffix == ".py":
                importlib.reload(module_dict[path.stem])
            elif path.is_dir():
                reload_package_recursive(path, module_dict[path.stem].__dict__)

    reload_package_recursive(Path(__file__).parent, module_dict_main)


if "bpy" in locals():
    reload_package(locals())


def all_classes() -> List[Type]:
    from owm_additions.bones.dev_find_common_bones import (
        OWM_ADD_DevFindCommonBones,
        OWM_ADD_DevFindFrequentBones,
    )
    from owm_additions.bones.dev_hide_all_bones_except import (
        OWM_ADD_Dev_Hide_All_Bones_Except,
    )
    from owm_additions.bones.dev_print_selected_bones import (
        OWM_ADD_Dev_Print_Selected_Bones_Dict,
        OWM_ADD_Dev_Print_Selected_Bones_List,
        OWM_ADD_Dev_Print_Selected_Bones_Set,
    )
    from owm_additions.bones.operator import OWM_ADD_UpdateArmature
    from owm_additions.dev.dev_allow_select_armatures_only import (
        OWM_ADD_Dev_Allow_Select_Armatures_Only,
    )
    from owm_additions.dev.dev_hide_all_empties import OWM_ADD_Dev_Hide_All_Empties
    from owm_additions.dev.dev_import_all_skins import OWM_ADD_DevImportAllSkins
    from owm_additions.dev.dev_prop import OWM_ADD_Dev_Props
    from owm_additions.hero_skins_prop import OWM_Hero_Skin
    from owm_additions.op_import_skin import OWM_ADD_ImportSkin
    from owm_additions.op_import_victory_pose import OWM_ADD_ImportVictoryPose
    from owm_additions.organize_hero_objs import OWM_ADD_Organize_Hero_Objects
    from owm_additions.ui import OWM_ADD_PT_DevPanelUI, OWM_ADD_PT_PanelUI

    return [
        OWM_ADD_NameProp,
        OWM_Hero_Skin,
        OWM_ADD_Dev_Props,
        OWM_ADD_UpdateArmature,
        OWM_ADD_Organize_Hero_Objects,
        OWM_ADD_ImportSkin,
        OWM_ADD_ImportVictoryPose,
        OWM_ADD_DevImportAllSkins,
        OWM_ADD_DevFindCommonBones,
        OWM_ADD_DevFindFrequentBones,
        OWM_ADD_Dev_Allow_Select_Armatures_Only,
        OWM_ADD_Dev_Hide_All_Bones_Except,
        OWM_ADD_Dev_Hide_All_Empties,
        OWM_ADD_Dev_Print_Selected_Bones_Dict,
        OWM_ADD_Dev_Print_Selected_Bones_List,
        OWM_ADD_Dev_Print_Selected_Bones_Set,
        OWM_ADD_PT_PanelUI,
        OWM_ADD_PT_DevPanelUI,
    ]


def register():
    for cls in all_classes():
        print(f"registering {cls}...")
        bpy.utils.register_class(cls)

    from owm_additions.dev.dev_prop import OWM_ADD_Dev_Props
    from owm_additions.hero_skins_prop import OWM_Hero_Skin

    bpy.types.Scene.owm_additions_hero_skin = bpy.props.PointerProperty(
        type=OWM_Hero_Skin
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


def unregister():
    for cls in all_classes():
        print(f"unregistering {cls}...")
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.owm_additions_hero_skin
    del bpy.types.Scene.owm_additions_dev_props

    IDStore = bpy.types.WindowManager
    del IDStore.owm_additions_hero_options
    del IDStore.owm_additions_skin_options
    del IDStore.owm_additions_victory_pose_options


if __name__ == "__main__":
    register()
