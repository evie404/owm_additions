from typing import Dict, Optional

from bpy.types import Armature, EditBone

from .mappings import BASE_BONE_GROUP_MAPPINGS, get_skin_bone_mapping
from .models.bone_group_mapping import BoneGroupMapping


def rename_all_bones(
    armature: Armature, character: Optional[str] = None, skin: Optional[str] = None
) -> None:
    rename_bones(armature, BASE_BONE_GROUP_MAPPINGS)
    rename_bones(armature, get_skin_bone_mapping(character, skin))


def rename_bones(armature: Armature, mappings: Dict[str, BoneGroupMapping]) -> None:
    for mapping in mappings.values():
        for bone_name in mapping.bones.keys():
            if mapping.bones[bone_name] == "":
                continue

            if bone_name not in armature.edit_bones:
                continue

            edit_bone: EditBone = armature.edit_bones[bone_name]
            edit_bone.name = mapping.bones[bone_name]
