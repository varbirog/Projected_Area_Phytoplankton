# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 12:22:32 2024

@author: VGabor
"""

# Run under VSCode with the command line: blender --background --python G:/Blender_3D/Code/ProjectedArea_checking.py


import bpy
import os
import math
import csv
import bmesh
from mathutils import Vector

# specify the directory where the obj files are located
dir_path = "G:/Blender_3D/Chlorophyceae"

# get list of all files in directory
file_list = os.listdir(dir_path)

# get list of obj files
obj_list = [item for item in file_list if item.endswith('.obj')]

# Create and open a CSV file for writing
csv_file = open('G:/Blender_3D/Chlorophyceae/rotation_check_all.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Object Number', 'Rotation X', 'Rotation Y', 'Rotation Z', 'Max Dim Index','dim_x','dim_y','dim_z',"total_area","volume"])


# loop through the obj files and import them one by one
for item in obj_list:
    path_to_file = os.path.join(dir_path, item)
    file_name = os.path.splitext(item)[0]
    # delete all mesh objects
    bpy.ops.object.select_all(action='SELECT')

    # Delete all selected objects
    bpy.ops.object.delete()
    
    # import obj
    bpy.ops.wm.obj_import(filepath=path_to_file)
    
    # Get the current scene
    scene = bpy.context.scene
    
    # Initialize object counter
    obj_counter = 1

    # Initialize list to store object data
    obj_data_list = []

   # Loop through all objects in the scene
    for obj in scene.objects:
        # Skip camera, light, and empty objects
        if obj.type in ['CAMERA', 'LIGHT', 'EMPTY']:
            continue

        # Calculate dimension
        dims = obj.dimensions
        dims_list = list(dims)
        max_dim = max(dims_list)
        # Find the index of the longest dimension
        max_dim_index = dims_list.index(max(dims_list))
        
        # If the longest dimension is not the Z-axis (index 2), rotate the object
        if max_dim_index != 2:
            # If the longest dimension was the X-axis (index 0), rotate 90 degrees around the Y-axis
            if max_dim_index == 0:
                obj.rotation_euler[1] = math.radians(90)
            # If the longest dimension was the Y-axis (index 1), rotate 90 degrees around the X-axis
            elif max_dim_index == 1:
                obj.rotation_euler[0] = math.radians(90)
        mesh = obj.data

        total_area = 0
        for p in mesh.polygons:
            total_area += p.area    

        bm = bmesh.new()
        bm.from_mesh(mesh)
        bm.transform(obj.matrix_world)
        bmesh.ops.triangulate(bm, faces=bm.faces)

        volume = 0
        for f in bm.faces:
            v1 = f.verts[0].co
            v2 = f.verts[1].co
            v3 = f.verts[2].co
            volume += v1.dot(v2.cross(v3)) / 6

        #print("Volume:", volume)

        bm.free()

        # Store the object data in a dictionary and append it to the list
        obj_data = {'file_name': file_name, 'obj_counter': obj_counter, 'rotation_x': math.degrees(obj.rotation_euler[0]), 'rotation_y': math.degrees(obj.rotation_euler[1]), 'rotation_z': math.degrees(obj.rotation_euler[2]), 'max_dim_index': max_dim_index, 'dims': dims, 'total_area': total_area, 'volume': volume}
        obj_data_list.append(obj_data)
      
        # Increment object counter
        obj_counter += 1

    # Sort the list of object data by volume
    obj_data_list.sort(key=lambda x: x['volume'], reverse=True)

    # Write the sorted object data to the CSV file
    for obj_data in obj_data_list:
        csv_writer.writerow([obj_data['file_name'],obj_data['obj_counter'],  obj_data['rotation_x'], obj_data['rotation_y'], obj_data['rotation_z'], obj_data['max_dim_index'], obj_data['dims'][0], obj_data['dims'][1], obj_data['dims'][2], obj_data['total_area'], obj_data['volume']])

# Close the CSV file
csv_file.close()

print("The pixel counts have been written to 'rotation_check_all.csv'.")
