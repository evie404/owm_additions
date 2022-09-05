from typing import Dict, Optional

import bpy
from bpy.types import BoneGroup, Object, PoseBone

from .mappings import BASE_BONE_GROUP_MAPPINGS, get_skin_bone_mapping
from .models.bone_group_mapping import BoneGroupMapping


def clear_bone_groups(armature_object: Object) -> None:
    for bone_group in armature_object.pose.bone_groups:
        armature_object.pose.bone_groups.remove(bone_group)


def assign_bone_groups(
    armature_object: Object, character: Optional[str] = None, skin: Optional[str] = None
) -> None:
    ungrouped = ensure_bone_group(armature_object, "Ungrouped")

    # assign everything to ungrouped
    for pose_bone in armature_object.pose.bones:
        pose_bone: PoseBone

        pose_bone.bone_group = ungrouped

    assign_bone_group(armature_object, BASE_BONE_GROUP_MAPPINGS)
    assign_bone_group(armature_object, get_skin_bone_mapping(character, skin))

    bpy.ops.pose.group_sort()


def assign_bone_group(
    armature_object: Object, mappings: Dict[str, BoneGroupMapping]
) -> None:
    for group_name, mapping in mappings.items():
        bone_group = ensure_bone_group(armature_object, group_name)

        for bone_name in mapping.bones.keys():
            if bone_name not in armature_object.pose.bones:
                continue

            pose_bone: PoseBone = armature_object.pose.bones[bone_name]

            pose_bone.bone_group = bone_group


def ensure_bone_group(armature_object: Object, group_name: str) -> BoneGroup:
    if group_name not in armature_object.pose.bone_groups:
        return armature_object.pose.bone_groups.new(name=group_name)

    return armature_object.pose.bone_groups[group_name]
