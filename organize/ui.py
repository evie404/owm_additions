import bpy
from bpy.types import Context, UILayout

from ..bones.op_update_armature import OWM_ADD_UpdateArmature
from ..importing.assets import HERO_SKINS
from .op_organize_hero_objs import OWM_ADD_Organize_Hero_Objects


class OWM_ADD_PT_OrganizePanel(bpy.types.Panel):
    bl_category = "OWM Additions"
    bl_label = "Organize OW Imports"
    bl_idname = "OWM_ADD_PT_OrganizePanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    # bl_context = "objectmode"
    # bl_options = {"DEFAULT_CLOSED"}

    # @classmethod
    # def poll(cls, context: Context) -> bool:
    #     if "owm.skeleton.model" in bpy.context.active_object.keys():
    #         return True

    #     if "owm.skeleton.name" in bpy.context.active_object.keys():
    #         return True

    #     return False

    def draw(self, context: Context) -> None:
        col = self.layout.column()

        self._draw_hero_search(col, context)
        self._draw_skin_search(col, context)

        col.operator(
            OWM_ADD_UpdateArmature.bl_idname,
            icon="ARMATURE_DATA",
        )

        col.operator(
            OWM_ADD_Organize_Hero_Objects.bl_idname,
            icon="OUTLINER_COLLECTION",
        )

    # TODO: reuse
    def _draw_hero_search(self, col: UILayout, context: Context) -> None:
        id_store = bpy.context.window_manager
        owm_additions_hero_options = id_store.owm_additions_hero_options

        owm_additions_hero_options.clear()

        for name in sorted(HERO_SKINS.keys()):
            item = owm_additions_hero_options.add()
            item.name = name

        col.prop_search(
            context.scene.owm_additions_import_assets,
            "hero",
            id_store,
            "owm_additions_hero_options",
            text="Hero",
        )

    # TODO: reuse
    def _draw_skin_search(self, col: UILayout, context: Context) -> None:
        id_store = bpy.context.window_manager
        owm_additions_skin_options = id_store.owm_additions_skin_options

        owm_additions_skin_options.clear()

        hero = context.scene.owm_additions_import_assets.hero
        skins = HERO_SKINS.get(hero, [])

        for name in skins:
            item = owm_additions_skin_options.add()
            item.name = name

        col.prop_search(
            context.scene.owm_additions_import_assets,
            "skin",
            id_store,
            "owm_additions_skin_options",
            text="Skin",
        )
