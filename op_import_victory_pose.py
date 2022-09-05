import os
from dataclasses import dataclass
from typing import Callable, List, Set, Tuple

import bpy
from bpy.types import Action, Context
from io_anim_seanim import import_seanim

from owm_additions.hero_skins_prop import (
    get_context_emote_name,
    get_context_hero_name,
    get_context_highlight_intro_name,
    get_context_victory_pose_name,
)
from owm_additions.paths.animation import (
    EMOTE_ANIMATION_TYPE,
    HIGHLIGHT_INTRO_ANIMATION_TYPE,
    VICTORY_POSE_ANIMATION_TYPE,
    animation_paths,
)


class OWM_ADD_ImportAnimationBase(bpy.types.Operator):
    bl_options = {"UNDO"}

    animation_type: str
    get_animation_name: Callable[[Context], str]

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
        animation_name = self.get_animation_name(context)

        import_set_hero_animations(context, hero, self.animation_type, animation_name)

        self.report({"INFO"}, f"Finished import {hero} ({animation_name}).")

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


class OWM_ADD_ImportVictoryPose(OWM_ADD_ImportAnimationBase):
    bl_idname = "owm_add.import_victory_pose"
    bl_label = "Import Victory Pose"

    animation_type = VICTORY_POSE_ANIMATION_TYPE

    def get_animation_name(self, context: Context) -> str:
        return get_context_victory_pose_name(context)


class OWM_ADD_ImportHighlightIntro(OWM_ADD_ImportAnimationBase):
    bl_idname = "owm_add.import_highlight_intro"
    bl_label = "Import Highlight Intro"

    animation_type = HIGHLIGHT_INTRO_ANIMATION_TYPE

    def get_animation_name(self, context: Context) -> str:
        return get_context_highlight_intro_name(context)


class OWM_ADD_ImportEmote(OWM_ADD_ImportAnimationBase):
    bl_idname = "owm_add.import_emote"
    bl_label = "Import Emote"

    animation_type = EMOTE_ANIMATION_TYPE

    def get_animation_name(self, context: Context) -> str:
        return get_context_emote_name(context)


def import_set_hero_animations(
    context: Context, hero: str, animation_type: str, animation_name: str
) -> None:
    filepaths = animation_paths(hero, animation_type, animation_name)

    actions = import_animations(context, filepaths)

    hero_actions, _ = group_and_rename_actions(hero, animation_name, actions)

    if len(hero_actions) > 0:
        set_action(context, hero_actions[0])


def group_and_rename_actions(
    hero: str, animation_name: str, actions: List[Action]
) -> Tuple[List[Action], List[Action]]:
    hero_actions: List[Action] = []
    misc_actions: List[Action] = []

    for action in actions:
        if len(action.fcurves) > 200:
            hero_actions.append(action)
        else:
            misc_actions.append(action)

    for hero_action in hero_actions:
        name = f"{hero} - {animation_name}"

        if len(misc_actions) > 0:
            name = name + " (Hero)"

        hero_action.name = name

    for misc_action in misc_actions:
        misc_action.name = f"{hero} - {animation_name} (Misc)"

    return (hero_actions, misc_actions)


def set_action(context: Context, action: Action) -> None:
    bpy.ops.object.mode_set(mode="POSE")

    context.active_object.animation_data.action = None

    bpy.ops.pose.reveal()
    bpy.ops.pose.reveal()
    bpy.ops.pose.select_all()
    bpy.ops.pose.transforms_clear()

    context.active_object.animation_data.action = action


@dataclass
class JankFile:
    name: str


@dataclass
class JankFiles:
    files: List[JankFile]


def import_animations(context: Context, filepaths: List[str]) -> List[Action]:
    actions: List[Action] = []

    # fuck this
    for filename in filepaths:
        jank_file = JankFile(os.path.basename(filename))
        jank_files = JankFiles([jank_file])

        import_seanim.load(jank_files, context, filename)

        action: Action = bpy.context.active_object.animation_data.action
        actions.append(action)

    return actions
