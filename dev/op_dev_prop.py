import bpy


class OWM_ADD_Dev_Props(bpy.types.PropertyGroup):
    bone_to_show: bpy.props.StringProperty()

    bone_frequency_threshold: bpy.props.FloatProperty(default=0.9, min=0, max=1.0)
