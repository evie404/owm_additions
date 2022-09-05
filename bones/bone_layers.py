from typing import Dict, Optional, Tuple

from bpy.types import Armature, EditBone

from .mappings import BASE_BONE_GROUP_MAPPINGS, get_skin_bone_mapping
from .bone_group_mapping import BoneGroupMapping


def clear_bone_layers(armature: Armature) -> None:
    empty_bone_layers: Tuple[bool, ...] = (
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
    )

    for edit_bone in armature.edit_bones:
        edit_bone: EditBone

        # set unknown layer
        edit_bone.layers = empty_bone_layers


def assign_bone_layers(
    armature: Armature, character: Optional[str] = None, skin: Optional[str] = None
) -> None:
    assign_bone_layer(armature, BASE_BONE_GROUP_MAPPINGS)
    assign_bone_layer(armature, get_skin_bone_mapping(character, skin))


def assign_bone_layer(
    armature: Armature, mappings: Dict[str, BoneGroupMapping]
) -> None:
    for mapping in mappings.values():
        for bone_name in mapping.bones.keys():
            if bone_name not in armature.edit_bones:
                continue

            edit_bone: EditBone = armature.edit_bones[bone_name]

            for i in mapping.layers:
                edit_bone.layers[i] = True

            if len(mapping.layers) > 0:
                edit_bone.layers[31] = False
