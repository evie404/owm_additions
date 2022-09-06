from typing import Dict, List, Optional, Set, Union

import bpy
from bpy.types import Bone, Context, EditBone, PoseBone


class OWM_ADD_Dev_Print_Bone_Children_Dict(bpy.types.Operator):
    bl_idname = "owm_add.dev_print_bone_children_dict"
    bl_label = "Print Children Bones (Dict)"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context):
        if not context.active_object:
            self.report({"ERROR_INVALID_CONTEXT"}, "Please select a OWM armature.")
            return {"CANCELLED"}

        obj = context.active_object

        if not (obj and obj.type == "ARMATURE"):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected object is not an armature."
            )

            return {"CANCELLED"}

        # print("wtf")
        # print(find_selected_bone(context))

        bone = find_selected_bone(context)
        if not bone:
            return {"FINISHED"}

        children = bone_children(bone)

        print(ordered_bones_dict(children))

        # print(ordered_bones_dict(selected_bones_children(context)))

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context) -> bool:
        return context.active_object and context.active_object.type == "ARMATURE"


def find_selected_bone(context: Context) -> Optional[Union[Bone, PoseBone, EditBone]]:
    if context.selected_bones and len(context.selected_bones) > 0:
        return context.selected_bones[0]

    if context.selected_editable_bones and len(context.selected_editable_bones) > 0:
        return context.selected_editable_bones[0]

    if context.selected_pose_bones and len(context.selected_pose_bones) > 0:
        return context.selected_pose_bones[0]

    return None


def bone_children(
    bone: Union[Bone, PoseBone, EditBone]
) -> List[Union[Bone, PoseBone, EditBone]]:
    if not bone:
        return []

    bones: List[Union[Bone, PoseBone, EditBone]] = [bone]

    while len(bone.children) > 0:
        bone = bone.children[0]
        bones.append(bone)

    return bones


def ordered_bones_dict(bones: List[Union[Bone, PoseBone, EditBone]]) -> Dict[str, str]:
    bones_dict: Dict[str, str] = {}

    for i, bone in enumerate(bones):
        bones_dict[bone.name] = str(i + 1)

    return bones_dict
