bl_info = {
    "name": "Nier: Automata Model Exporter",
    "author": "Woeful_Wolf",
    "version": (1, 1),
    "blender": (2, 80, 0),
    "location": "File > Import-Export",
    "description": "Export Blender model to Nier:Automata wmb model data",
    "category": "Import-Export"}

import bpy
from bpy_extras.io_utils import ExportHelper,ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty

class ExportBlender2Nier(bpy.types.Operator, ExportHelper):
    '''Export a Nier: Automata WMB File.'''
    bl_idname = "export.wmb_data"
    bl_label = "Export WMB Data"
    bl_options = {'PRESET'}
    filename_ext = ".wmb"
    filter_glob: StringProperty(default="*.wmb", options={'HIDDEN'})

    def execute(self, context):
        from blender2nier import wmb_exporter
        return wmb_exporter.main(self.filepath)

def menu_func_export(self, context):
    self.layout.operator_context = 'INVOKE_DEFAULT'
    self.layout.operator(ExportBlender2Nier.bl_idname, text="WMB File for Nier: Automata (.wmb)")


def register():
    bpy.utils.register_class(ExportBlender2Nier)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExportBlender2Nier)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == '__main__':
    register()