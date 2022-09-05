from typing import Optional

import bpy
from bpy.types import Armature, Collection, Context, Object

from .hero_skins_prop import get_context_hero_name, get_context_skin_name


class OWM_ADD_Organize_Hero_Objects(bpy.types.Operator):
    bl_idname = "owm_add.org_hero_objects"
    bl_label = "Organize Hero Objects"
    # bl_description = "Clear all bones and object transformations"
    bl_options = {"UNDO"}

    def execute(self, context: Context):
        obj = bpy.context.active_object

        root_obj = find_root(context)

        if not root_obj:
            self.report(
                {"ERROR_INVALID_CONTEXT"}, "Please select an object of the hero."
            )

            return {"CANCELLED"}

        hero = get_context_hero_name(context)
        skin = get_context_skin_name(context)

        ow_organize_character_objects(
            collection=context.collection,
            root_object=root_obj,
            hero=hero,
            skin=skin,
        )

        self.report({"INFO"}, f"Finished updating armature with {hero} ({skin}).")

        return {"FINISHED"}

    # @classmethod
    # def poll(cls, context: Context) -> bool:
    #     return (
    #         context.active_object
    #         and context.active_object.type == "ARMATURE"
    #         and "owm.skeleton.model" in context.active_object.keys()
    #         and "owm.skeleton.name" in context.active_object.keys()
    #     )


def find_root(context: Context) -> Optional[Object]:
    obj: Object = context.object

    while obj:
        if obj.name == "Entity HeroGallery":
            return obj

        obj = obj.parent

    return None


def ensure_collection_in(parent: Collection, name: str) -> Collection:
    if name in parent.children:
        return parent.children[name]

    collection = bpy.data.collections.new(name)
    parent.children.link(collection)

    return collection


def ow_organize_character_objects(
    collection: Collection, root_object: Object, hero: str, skin: str
) -> None:
    name = f"{hero} ({skin})"
    name_prefixed = name + " - "

    collection.name = name

    arm_collection = ensure_collection_in(collection, name_prefixed + "Armatures")

    char_mesh_collection = ensure_collection_in(
        collection, name_prefixed + "Character Mesh"
    )

    char_mesh_unused_collection = ensure_collection_in(
        char_mesh_collection, name_prefixed + "Character Mesh (Unused)"
    )

    weapon_mesh_collection = ensure_collection_in(
        collection, name_prefixed + "Weapons Mesh"
    )

    hardpoints_collection = ensure_collection_in(
        collection, name_prefixed + "Hardpoints"
    )

    root_object.name = name_prefixed + "Character Root"

    for obj in collection.objects:
        obj: Object

        if not obj.name.startswith(name_prefixed):
            obj.name = name_prefixed + obj.name

        if "hardpoint" in obj.name and obj.name not in hardpoints_collection.objects:
            collection.objects.unlink(obj)
            hardpoints_collection.objects.link(obj)

        if obj.type == "ARMATURE" and obj.name not in arm_collection.objects:
            arm_collection.objects.link(obj)

        # if obj.name == root.name or obj.type != "EMPTY":
        #     continue

        # obj.

    # organize character armature
    highest_bones = 0
    biggest_armature: Object

    for obj in arm_collection.objects:
        armature: Armature = obj.data

        num_bones = len(armature.bones)
        if num_bones > highest_bones:
            highest_bones = num_bones

            biggest_armature = obj

    biggest_armature.name = name_prefixed + "Character Armature"

    # organize weapon armatures
    for obj in arm_collection.objects:
        if obj.name == biggest_armature.name:
            continue

        if not obj.name.endswith(".001"):
            continue

        orig_name = obj.name.removesuffix(".001")
        orig_obj: Object = arm_collection.objects[orig_name]

        if orig_obj.matrix_world.translation.x > 0:
            orig_obj.name = orig_name + " L"
            obj.name = orig_name + " R"
        else:
            orig_obj.name = orig_name + " R"
            obj.name = orig_name + " L"

        obj.data = orig_obj.data
        obj.data.name = orig_obj.name

    # organize weapon meshes
    for arm_obj in arm_collection.objects:
        arm_obj: Object

        if arm_obj.name == biggest_armature.name:
            continue

        for child in arm_obj.children:
            child: Object

            if child.type != "MESH":
                continue

            if not child.name.endswith(".001"):
                continue

            orig_name = child.name.removesuffix(".001")
            orig_obj: Object = bpy.data.objects[orig_name]

            child.data = orig_obj.data
            child.data.name = orig_obj.name

    for arm_obj in arm_collection.objects:
        arm_obj: Object

        if arm_obj.name == biggest_armature.name:
            continue

        suffix: Optional[str] = None

        if arm_obj.name.endswith(" R") or arm_obj.name.endswith(" L"):
            suffix = arm_obj.name[-2:]

        mesh_collection = ensure_collection_in(weapon_mesh_collection, arm_obj.name)

        for child in arm_obj.children:
            child: Object

            if child.type != "MESH":
                continue

            if child.name not in mesh_collection.objects:
                collection.objects.unlink(child)
                mesh_collection.objects.link(child)

            if suffix:
                if child.name.endswith(".001"):
                    child.name = child.name.replace(".001", suffix)
                else:
                    child.name = child.name + suffix

    # organize character meshes
    for child in biggest_armature.children:
        if child.type != "MESH":
            continue

        if child.name not in char_mesh_collection.objects:
            collection.objects.unlink(child)
            char_mesh_collection.objects.link(child)

    # for obj in arm_collection.objects:
