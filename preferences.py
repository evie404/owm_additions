import bpy
from bpy.props import BoolProperty, StringProperty


class OWM_ADD_Preferences(bpy.types.AddonPreferences):
    bl_idname = "owm_additions"

    show_experimental_features: BoolProperty(
        name="Show Experimental Features", default=False
    )
    show_development_features: BoolProperty(
        name="Show Development-Only Features", default=False
    )

    def draw(self, context):
        layout = self.layout

        row = layout.row()

        col = row.column(align=True)
        col.label(text="Features:")
        col.prop(self, "show_experimental_features")
        col.prop(self, "show_development_features")
