rld = False

if "bpy" in locals():
    import imp

    rld = True

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

if rld:
    imp.reload(update_bones)

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
