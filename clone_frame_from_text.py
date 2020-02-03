import bpy
from random import randint

class NODES_OP_clone_frame(bpy.types.Operator):
    """Clone frame from text"""
    bl_idname = "node.clone_frame_from_text"
    bl_label = "Clone frame from text"

    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR' and context.active_node and context.active_node.type == 'FRAME'

    def execute(self, context):
        print('execute!')
        print(context.area.type)
        print(context.area)
        print(context.active_node)
        print(dir(context.active_node))
        active_node = context.active_node
        w, h = active_node.dimensions
        bpy.ops.node.duplicate()
        bpy.ops.node.translate_attach(TRANSFORM_OT_translate={'value': (0, -h - 10, 0)})
        context.active_node.label = str(randint(0, 20))
        return {'FINISHED'}

def register():
    print('reg')
    bpy.utils.register_class(NODES_OP_clone_frame)

def unregister():
    print('unreg')
    bpy.utils.unregister_class(NODES_OP_clone_frame)

if __name__ == "__main__":
    register()


