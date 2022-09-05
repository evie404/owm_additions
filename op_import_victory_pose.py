import os
from dataclasses import dataclass
from typing import List, Set

import bpy
from bpy.types import Action, Context
from io_anim_seanim import import_seanim

from owm_additions.hero_skins_prop import (
    get_context_hero_name,
    get_context_victory_pose_name,
)
from owm_additions.paths.victory_pose import victory_pose_animation_paths


@dataclass
class JankFile:
    name: str


@dataclass
class JankFiles:
    files: List[JankFile]


class OWM_ADD_ImportVictoryPose(bpy.types.Operator):
    bl_idname = "owm_add.import_victory_pose"
    bl_label = "Import Victory Pose"
    # bl_description = "Clear all bones and object transformations"
    bl_options = {"UNDO"}

    def execute(self, context: Context) -> Set[str]:
        if not bpy.context.active_object:
            self.report({"ERROR_INVALID_CONTEXT"}, "Please select a OWM armature.")
            return {"CANCELLED"}

        obj = bpy.context.active_object

        if not (obj and obj.type == "ARMATURE"):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected object is not an armature."
            )

            return {"CANCELLED"}

        if (
            "owm.skeleton.model" not in obj.keys()
            and "owm.skeleton.name" not in obj.keys()
        ):
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Selected armature is not an OWM armature."
            )
            return {"CANCELLED"}

        hero = get_context_hero_name(context)
        victory_pose = get_context_victory_pose_name(context)

        victory_pose_paths = victory_pose_animation_paths(hero, victory_pose)

        actions: List[Action] = []

        hero_actions: List[Action] = []
        misc_actions: List[Action] = []

        # fuck this
        for filename in victory_pose_paths:
            jank_file = JankFile(os.path.basename(filename))
            jank_files = JankFiles([jank_file])

            import_seanim.load(jank_files, context, filename)

            action: Action = bpy.context.active_object.animation_data.action
            if len(action.fcurves) > 200:
                hero_actions.append(action)
            else:
                misc_actions.append(action)

        if len(hero_actions) > 0:
            bpy.context.active_object.animation_data.action = None

            bpy.ops.pose.reveal()
            bpy.ops.pose.reveal()
            bpy.ops.pose.select_all()
            bpy.ops.pose.transforms_clear()

            bpy.context.active_object.animation_data.action = hero_actions[0]

        for hero_action in hero_actions:
            name = f"{hero} - {victory_pose}"

            if len(misc_actions) > 0:
                name = name + " (Hero)"

            hero_action.name = name

        for misc_action in misc_actions:
            misc_action.name = f"{hero} - {victory_pose} (Misc)"

        self.report({"INFO"}, f"Finished import {hero} ({victory_pose}).")

        return {"FINISHED"}

    @classmethod
    def poll(cls, context: Context) -> bool:
        return (
            context.mode == "OBJECT"
            and context.active_object
            and context.active_object.type == "ARMATURE"
            and "owm.skeleton.model" in context.active_object.keys()
            and "owm.skeleton.name" in context.active_object.keys()
        )
