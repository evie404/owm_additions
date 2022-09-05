from typing import Dict, List, Tuple

import bpy
from bpy.props import EnumProperty
from bpy.types import Context

from .hero_skins import HERO_SKINS, HERO_UNICODED, SKIN_UNICODED


def all_skin_options() -> List[Tuple[str, str, str]]:
    options: List[Tuple[str, str, str]] = []

    for hero, skins in HERO_SKINS.items():
        for skin in skins:
            options.append((f"owm_additions.hero.{hero}.{skin}", skin, ""))

    return options


def skin_options(self, context: Context) -> List[Tuple[str, str, str]]:
    # print("skin_options")

    # print(f"self: {self} ({type(self)})")

    # print(
    #     f"context.scene.owm_additions_hero_skin.hero: {context.scene.owm_additions_hero_skin.hero} ({type(context.scene.owm_additions_hero_skin.hero)})"
    # )

    hero = get_context_hero_name(context)

    skins = HERO_SKINS.get(hero)
    # print(f"skins: {skins}")

    if not skins:
        return []

    options: List[Tuple[str, str, str]] = []

    for skin in skins:
        options.append((owm_addition_skin_option(skin), skin, ""))

    # context.scene.owm_additions_hero_skin.skin = None
    # print(
    #     f"context.scene.owm_additions_hero_skin.skin: {context.scene.owm_additions_hero_skin.skin} ({type(context.scene.owm_additions_hero_skin.skin)})"
    # )

    return options


def get_context_hero_name(context: Context) -> str:
    return owm_addition_hero_unoption(context.scene.owm_additions_hero_skin.hero)


def get_context_skin_name(context: Context) -> str:
    return owm_addition_skin_unoption(context.scene.owm_additions_hero_skin.skin)


HERO_OPTION_PREFIX = "owm_additions.hero."
SKIN_OPTION_PREFIX = "owm_additions.skin."


def owm_addition_option(prefix: str, name: str) -> str:
    return prefix + name.encode("ascii", "ignore").decode()


def owm_addition_unoption(
    prefix: str, option: str, unicoded_dict: Dict[str, str]
) -> str:
    ascii_name = option.removeprefix(prefix)
    return unicoded_dict.get(ascii_name) or ascii_name


def owm_addition_hero_option(hero: str) -> str:
    return owm_addition_option(HERO_OPTION_PREFIX, hero)


def owm_addition_hero_unoption(hero_option: str) -> str:
    return owm_addition_unoption(HERO_OPTION_PREFIX, hero_option, HERO_UNICODED)


def owm_addition_skin_option(skin: str) -> str:
    return owm_addition_option(SKIN_OPTION_PREFIX, skin)


def owm_addition_skin_unoption(skin_option: str) -> str:
    return owm_addition_unoption(SKIN_OPTION_PREFIX, skin_option, SKIN_UNICODED)


def update_skin_selection(self, context: Context) -> None:
    print("update_skin_selection")

    print(f"self: {self} ({type(self)})")

    # self.

    print(
        f"context.scene.owm_additions_hero_skin.skin: {context.scene.owm_additions_hero_skin.skin} ({type(context.scene.owm_additions_hero_skin.skin)})"
    )

    context.scene.owm_additions_hero_skin.skin = None


class OWM_Hero_Skin(bpy.types.PropertyGroup):
    heroes = [
        (owm_addition_hero_option(hero), hero, "", hero, i)
        for i, hero in enumerate(HERO_SKINS.keys())
    ]

    # TODO: reset skin when hero changes
    skin: EnumProperty(
        items=skin_options,
        # name="Description for the Elements",
        # default="A",
        # description="Tooltip for the Dropdownbox",
    )

    hero: bpy.props.EnumProperty(
        # update=update_skin_selection,
        items=heroes,
        # description="",
        # default=f"owm_additions.hero.{HERO_NAMES[0]}",
        # update=execute_operator,
    )
