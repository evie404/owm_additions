from typing import List, Set

import bpy
from bpy.types import Context, Object

from ..bones.update_bones import update_bones
from ..importing.asset_prop import get_context_hero_name


class OWM_ADD_Dev_Apply_Base_Mapping_To_All(bpy.types.Operator):
    bl_idname = "owm_add.dev_apply_base_mapping_to_all"
    bl_label = "Apply Base Mapping to All"
    # bl_description = "Clear all bones and object transformations"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        hero = get_context_hero_name(context)

        apply_base_mapping_to_all(context, hero, all_armature_objects())

        # self.report({"INFO"}, f"Finished importing all skins of {hero}.")

        return {"FINISHED"}


def all_armature_objects() -> List[Object]:
    arm_objs: List[Object] = []

    for obj in bpy.data.objects:
        obj: Object

        if obj.type != "ARMATURE":
            continue

        arm_objs.append(obj)

    return arm_objs


def apply_base_mapping_to_all(
    context: Context, hero: str, arm_objs: List[Object]
) -> None:
    for obj in arm_objs:
        update_bones(context, obj, hero, "Base")
