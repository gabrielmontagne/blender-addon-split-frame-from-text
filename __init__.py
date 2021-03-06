from bpy.props import StringProperty
from random import randint
import bpy

bl_info = {
    'name': 'Split Frame from Text Strip',
    'author': 'gabriel montagné, gabriel@tibas.london',
    'version': (0, 0, 1),
    'blender': (2, 80, 0),
    'description': 'Split a node editor frame from the contents of a text file',
    'tracker_url': 'https://github.com/gabrielmontagne/blender-addon-clone-frame-from-text/issues'
}

MARGIN = 15

class NODES_OP_split_frame(bpy.types.Operator):
    """Split frame from text"""
    bl_idname = "node.split_frame_from_text"
    bl_label = "Split Frame From Text"

    from_file: StringProperty(name='File')

    def draw(self, context):
        layout = self.layout
        layout.prop_search(self, "from_file", bpy.data, 'texts')

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR' and context.active_node and context.active_node.type == 'FRAME'

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        active_node = context.active_node
        w, h = active_node.dimensions

        lines = [l.body.strip() for l in bpy.data.texts[self.from_file].lines if l.body.strip()]
        assert len(lines), 'Should have at least one line'

        active_node.label= lines[0]

        for line in lines[1:]:
            bpy.ops.node.duplicate()
            bpy.ops.node.translate_attach(TRANSFORM_OT_translate={'value': (0, -(h + MARGIN), 0)})
            context.active_node.label = line

        return {'FINISHED'}

def register():
    bpy.utils.register_class(NODES_OP_split_frame)

def unregister():
    bpy.utils.unregister_class(NODES_OP_split_frame)

if __name__ == "__main__":
    register()
