import bpy
from bpy.types import Context

from .assets import HERO_SKINS


def get_context_hero_name(context: Context) -> str:
    return context.scene.owm_additions_import_assets.hero


def set_context_hero_name(context: Context, hero: str) -> None:
    context.scene.owm_additions_import_assets.hero = hero


def get_context_skin_name(context: Context) -> str:
    return context.scene.owm_additions_import_assets.skin


def set_context_skin_name(context: Context, skin: str) -> None:
    context.scene.owm_additions_import_assets.skin = skin


def get_context_victory_pose_name(context: Context) -> str:
    return context.scene.owm_additions_import_assets.victory_pose


def set_context_victory_pose_name(context: Context, victory_pose: str) -> None:
    context.scene.owm_additions_import_assets.victory_pose = victory_pose


def get_context_highlight_intro_name(context: Context) -> str:
    return context.scene.owm_additions_import_assets.highlight_intro


def set_context_highlight_intro_name(context: Context, highlight_intro: str) -> None:
    context.scene.owm_additions_import_assets.highlight_intro = highlight_intro


def get_context_emote_name(context: Context) -> str:
    return context.scene.owm_additions_import_assets.emote


def set_context_emote_name(context: Context, emote: str) -> None:
    context.scene.owm_additions_import_assets.emote = emote


def update_hero(self, context: Context) -> None:
    set_context_skin_name(context, "Classic")
    set_context_victory_pose_name(context, "Heroic")

    set_context_emote_name(context, "Heroic")
    set_context_highlight_intro_name(context, "")


class OWM_Asset_Prop(bpy.types.PropertyGroup):
    hero: bpy.props.StringProperty(
        default=list(HERO_SKINS.keys())[0],
        update=update_hero,
    )

    skin: bpy.props.StringProperty(default="Classic")

    victory_pose: bpy.props.StringProperty(default="Heroic")

    highlight_intro: bpy.props.StringProperty()

    emote: bpy.props.StringProperty(default="Heroic")
