from typing import Dict, Set

import bpy
from bpy.types import Armature, Context

from .mappings import BASE_BONE_GROUP_MAPPINGS


class OWM_ADD_DevFindCommonBones(bpy.types.Operator):
    bl_idname = "owm_add.dev_find_common_bones"
    bl_label = "Find Common Bones"

    def execute(self, context: Context) -> Set[str]:
        # TODO: exclude base bones
        common_bones = find_common_bones() - all_common_bones()

        print(f"common_bones: {set_to_dict(common_bones)}")

        return {"FINISHED"}


# class OWM_ADD_DevFindCommonBonesExceptGlobal(bpy.types.Operator):
#     bl_idname = "owm_add.dev_find_common_bones_except_global"
#     bl_label = "Find Common Bones (Except Global)"

#     def execute(self, context: Context) -> Set[str]:
#         common_bones = find_common_bones() - all_common_bones()

#         print(f"common_bones: {common_bones}")

#         return {"FINISHED"}


class OWM_ADD_DevFindFrequentBones(bpy.types.Operator):
    bl_idname = "owm_add.dev_find_frequent_bones"
    bl_label = "Find Frequent Bones"

    def execute(self, context: Context) -> Set[str]:
        # TODO: exclude base bones
        frequent_bones = find_frequent_bones(0.9) - all_common_bones()

        print(f"frequent_bones: {set_to_dict(frequent_bones)}")

        return {"FINISHED"}


def find_frequent_bones(threshold: float = 0.9) -> Set[str]:
    frequent_bones: Set[str] = set()
    bone_count: Dict[str, int] = {}

    threshold_count = int(len(bpy.data.armatures) * threshold)

    for armature in bpy.data.armatures:
        armature: Armature

        for bone in armature.bones:
            if bone.name not in bone_count:
                bone_count[bone.name] = 0

            bone_count[bone.name] += 1

    for bone, count in bone_count.items():
        if count >= threshold_count:
            frequent_bones.add(bone)

    return frequent_bones


def all_common_bones() -> Set[str]:
    bones: Set[str] = set()

    for mapping in BASE_BONE_GROUP_MAPPINGS.values():
        bones = bones.union(set(mapping.bones.keys()))

    return bones


def find_common_bones() -> Set[str]:
    common_bones: Set[str] = set()

    for i, armature in enumerate(bpy.data.armatures):
        armature: Armature

        # if i > 2:
        #     break

        # print(f"{i}: {armature.name}")

        # if len(armature.bones) < 100:
        #     continue

        if i == 0:
            for bone in armature.bones:
                common_bones.add(bone.name)
        else:
            current_bones: Set[str] = set()

            for bone in armature.bones:
                current_bones.add(bone.name)

            # print(f"current_bones: {current_bones}")
            # print(f"common_bones: {common_bones}")

            common_bones = common_bones.intersection(current_bones)

    # print(f"common_bones: {common_bones}")

    return common_bones


def set_to_dict(s: Set[str]) -> Dict[str, str]:
    d: Dict[str, str] = {}

    for item in s:
        d[item] = ""

    return d
