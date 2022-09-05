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
    from .hero_skins_prop import OWM_Hero_Skin
    from .bones.operator import OWM_ADD_UpdateArmature
    from .organize_hero_objs import OWM_ADD_Organize_Hero_Objects
    from .ui import OWM_ADD_PanelUI

    return [
        OWM_Hero_Skin,
        OWM_ADD_UpdateArmature,
        OWM_ADD_Organize_Hero_Objects,
        OWM_ADD_PanelUI,
    ]


def register():
    import bpy

    for cls in all_classes():
        print(f"registering {cls}...")
        bpy.utils.register_class(cls)

    from .hero_skins_prop import OWM_Hero_Skin

    bpy.types.Scene.owm_additions_hero_skin = bpy.props.PointerProperty(
        type=OWM_Hero_Skin
    )


def unregister():
    import bpy

    for cls in all_classes():
        print(f"unregistering {cls}...")
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.owm_additions_hero_skin


if __name__ == "__main__":
    register()
