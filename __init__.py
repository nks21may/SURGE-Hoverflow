bl_info = {
    "name": "SURGE Hoverflow",
    "author": "Kompile",
    "version": (1, 0),
    "blender": (4, 2, 1),
    "location": "View3D > Sidebar",
    "description": "Generates surf ramps for source engine games",
    "category": "Add Mesh",
}

from . import surf_ramp_generator

def register():
    surf_ramp_generator.register()

def unregister():
    surf_ramp_generator.unregister()