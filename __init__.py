bl_info = {
    "name": "Remove Custom Splitnormals",
    "description": "When importing 3D File Formats from different sources, custom splitnormals sometimes causing normal artifacts. To clean the object, the script will remove the custom split normals. So Blender can manage the normals the \"normal\" way.",
    "version": (0, 1, 00),
    "blender": (3, 0, 0),
    "category": "Mesh",
    "author": "3ddy",
    "location": "Object > Remove Custom Splitnormals"    
}

import bpy


def main(context):
    selection = bpy.context.selected_objects

    for obj in selection:
        bpy.context.view_layer.objects.active = obj
        bpy.ops.mesh.customdata_custom_splitnormals_clear()


class RemoveCustomSplitnormals(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.remove_custom_splitnormals"
    bl_label = "Remove Custom Splitnormals"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(RemoveCustomSplitnormals.bl_idname, text=RemoveCustomSplitnormals.bl_label)

def register():
    bpy.utils.register_class(RemoveCustomSplitnormals)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(RemoveCustomSplitnormals)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.object.remove_custom_splitnormals()
