# idTech 4 func_static entities exporting script 08/21/2023
# by jango___ (Madison Z.), nuesb and motorsep (all from Blender Discord chat).
# Objects that are needed to be exported as func_static entities should have corresponding ASE/LWO models already in place and
# have custom property type of String "model" to have value of path to the ASE/LWO model as it should be in .map file.
# Only selected objects will be saved.
# Use appropriate object name in Blender for proper referencing in the .map
# Please make sure to adjust path and filename to .map file where entities will be saved
import bpy
import mathutils
import numpy as np

outstr = ""
objects = bpy.context.selected_objects

for obj in objects:
    matrix = mathutils.Euler((-obj.rotation_euler.x,obj.rotation_euler.y,obj.rotation_euler.z)).to_matrix()
    tmatrix = np.transpose(matrix)
    #print(tmatrix)
    locVec = obj.location[:]
    formattedLocVec = " ".join([f"{coord:.7f}" for coord in locVec])
    outstr += f"""{{
    "classname" "func_static"
    "name" "{obj.name}"
    "origin" "{formattedLocVec}"
    "rotation" "{' '.join([str(i) for i in tmatrix.flatten()])}"
    "model" {obj["model"]}
}}
"""
# change path to the .map file where entities will be saved and the filename
with open("F:/Games/Phaeton/base/maps/test_entities.map", "w") as f:
    f.write(outstr)