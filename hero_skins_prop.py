import bpy
from bpy.types import Context

from .hero_skins import HERO_SKINS


def get_context_hero_name(context: Context) -> str:
    return context.scene.owm_additions_hero_skin.hero


def set_context_hero_name(context: Context, hero: str) -> None:
    context.scene.owm_additions_hero_skin.hero = hero


def get_context_skin_name(context: Context) -> str:
    return context.scene.owm_additions_hero_skin.skin


def set_context_skin_name(context: Context, skin: str) -> None:
    context.scene.owm_additions_hero_skin.skin = skin


def update_hero(self, context: Context) -> None:
    set_context_skin_name(context, "Classic")


class OWM_Hero_Skin(bpy.types.PropertyGroup):
    skin: bpy.props.StringProperty(default="Classic")
    hero: bpy.props.StringProperty(
        default=list(HERO_SKINS.keys())[0],
        update=update_hero,
    )
