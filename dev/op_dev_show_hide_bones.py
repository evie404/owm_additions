from typing import List, Set

import bpy
from bpy.types import Armature, Context, Object, PoseBone


class OWM_ADD_Dev_Hide_All_Bones_Except(bpy.types.Operator):
    bl_idname = "owm_add.dev_hide_all_bones_except"
    bl_label = "Hide All Bones Except"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context) -> Set[str]:
        if not context.active_object:
            self.report({"ERROR_INVALID_CONTEXT"}, "Please select a OWM armature.")
            return {"CANCELLED"}

        obj = context.active_object

        if not (obj and obj.type == "ARMATURE"):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected object is not an armature."
            )

            return {"CANCELLED"}

        # hide_all_empties()

        arm_objs = all_armature_objects()
        show_all_bones(context, arm_objs)

        # set_bone_constraints(arm_objs)

        reset_bones(arm_objs[0])

        bone_name = context.scene.owm_additions_dev_props.bone_to_show

        hide_all_bones_except(context, arm_objs, bone_name)
        # set_bone_offset(arm_objs[0], bone_name)

        context.view_layer.objects.active = arm_objs[0]
        bpy.ops.object.mode_set(mode="POSE")

        return {"FINISHED"}


class OWM_ADD_Dev_Show_All_Bones(bpy.types.Operator):
    bl_idname = "owm_add.dev_show_all_bones"
    bl_label = "Show All Bones"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context) -> Set[str]:
        arm_objs = all_armature_objects()

        show_all_bones(context, arm_objs)

        return {"FINISHED"}


class OWM_ADD_Dev_Show_Only_Unknown_Bones(bpy.types.Operator):
    bl_idname = "owm_add.dev_show_only_unknown_bones"
    bl_label = "Show Only Unknown Bones"
    # bl_description = "Clear all bones and object transformations"

    def execute(self, context: Context) -> Set[str]:
        arm_objs = all_armature_objects()

        show_only_unknown_bones(context, arm_objs)

        return {"FINISHED"}


def show_only_unknown_bones(context: Context, arm_objs: List[Object]) -> None:
    for obj in arm_objs:
        context.view_layer.objects.active = obj

        armature: Armature = obj.data

        for i in range(len(armature.layers)):
            armature.layers[i] = False

        armature.layers[31] = True


def show_all_bones(context: Context, arm_objs: List[Object]) -> None:
    for obj in arm_objs:
        context.view_layer.objects.active = obj

        armature: Armature = obj.data

        for i in range(len(armature.layers)):
            armature.layers[i] = True

        bpy.ops.object.mode_set(mode="POSE")

        bpy.ops.pose.select_all(action="DESELECT")

        bpy.ops.pose.reveal()
        bpy.ops.pose.reveal()

        bpy.ops.pose.select_all(action="DESELECT")

        bpy.ops.object.mode_set(mode="OBJECT")


def hide_all_bones_except(
    context: Context, arm_objs: List[Object], bone_name: str
) -> None:
    for obj in arm_objs:
        context.view_layer.objects.active = obj

        bpy.ops.object.mode_set(mode="POSE")
        # bpy.ops.object.posemode_toggle()

        bpy.ops.pose.reveal()
        bpy.ops.pose.reveal()

        bpy.ops.pose.select_all(action="DESELECT")

        bone = obj.data.bones.get(bone_name)
        if not bone:
            print(f"{bone} not found in {obj.name}.")

        context.object.data.bones.active = bone

        bpy.ops.pose.hide(unselected=True)

        # bpy.ops.object.posemode_toggle()

        bpy.ops.object.mode_set(mode="OBJECT")

        # for bone in obj.pose.bones:
        #     bone: PoseBone

        #     if bone.name != bone_name:
        #         bone.is_property_hidden


def all_armature_objects() -> List[Object]:
    arm_objs: List[Object] = []

    for obj in bpy.data.objects:
        obj: Object

        if obj.type != "ARMATURE":
            continue

        arm_objs.append(obj)

    return arm_objs


def copy_armature_pose_bones(
    source_armature: Object, destination_armature: Object
) -> None:
    for bone in destination_armature.pose.bones:
        bone: PoseBone

        if source_armature.pose.bones.get(bone.name) is None:
            continue

        for constraint in bone.constraints:
            bone.constraints.remove(constraint)

        constraint = bone.constraints.new("COPY_TRANSFORMS")
        constraint.target = source_armature
        constraint.subtarget = bone.name
        constraint.owner_space = "LOCAL"
        constraint.target_space = "LOCAL"


def set_bone_constraints(arm_objs: List[Object]) -> None:
    src = arm_objs[0]

    for obj in arm_objs[1:]:
        copy_armature_pose_bones(src, obj)

    return


def reset_bones(arm_obj: Object) -> None:
    for bone in arm_obj.pose.bones:
        bone: PoseBone

        bone.location = (0, 0, 0)


def set_bone_offset(arm_obj: Object, bone_name: str) -> None:
    arm_obj.pose.bones[bone_name].location = (1, 1, 1)
