import os
from dataclasses import dataclass
from typing import List, Set

import bpy
from bpy.types import Context
from io_anim_seanim import import_seanim

from owm_additions.hero_skins_prop import (
    get_context_hero_name,
    get_context_victory_pose_name,
)
from owm_additions.paths.victory_pose import animation_paths


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

        victory_pose_paths = animation_paths(hero, victory_pose)

        # fuck this
        filename = victory_pose_paths[0]

        jank_file = JankFile(os.path.basename(filename))
        jank_files = JankFiles([jank_file])

        import_seanim.load(jank_files, context, filename)

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
