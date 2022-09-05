from .operator import OWM_ADD_UpdateArmature
from .ui import OWM_ADD_PT_UpdateArmatureUI
from .update_bones import update_bones

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

import bpy

CLASSES = (OWM_ADD_UpdateArmature, OWM_ADD_PT_UpdateArmatureUI)


def register():
    for cls in CLASSES:
        print(f"registering {cls}...")
        bpy.utils.register_class(cls)


def unregister():
    for cls in CLASSES:
        print(f"unregistering {cls}...")
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
