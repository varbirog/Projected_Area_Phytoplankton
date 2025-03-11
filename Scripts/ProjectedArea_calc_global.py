# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 10:02:06 2024

@author: Gabor Varbiro
"""
# Run under VSCode with the command line: blender --background --python G:/Blender_3D/Code/ProjectedArea_calc_global.py

import bpy
import os
import math

# Reset the coordinates (x, y, z) 
x = 0.0
y = 0.0
z = 0.0

# Set the rotation increment
rotation_increment_f = 2  # degrees of tilt angle 
rotation_increment = 2  # degrees of rotataion angle
# Set the number of rotations (360 degrees)
num_rotations = int(180 / rotation_increment)
num_rotations_fall = int(90/rotation_increment_f)

# specify the directory where the obj files are located
dir_path = "Sample/Objects"

# get list of all files in directory
file_list = os.listdir(dir_path)
# Set render output directory
render_output_directory = bpy.path.abspath("Sample/Render_output")
# get list of obj files
obj_list = [item for item in file_list if item.endswith('.obj')]

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
 
 #Select the object 
    obj = bpy.data.objects[0]
    # Get the current scene
    scene = bpy.context.scene
     
    # Calculate dimension
    dims = obj.dimensions
    dims_list = list(dims)
    max_dim = max(dims_list)
    # Find the index of the longest dimension
    max_dim_index = dims_list.index(max(dims_list))
    
    # If the longest dimension is not the Z-axis (index 2), rotate the object
    if max_dim_index != 2:
        obj.rotation_euler[0] = math.radians(0)
        obj.rotation_euler[1] = math.radians(0)
        # If the longest dimension was the X-axis (index 0), rotate 90 degrees around the Y-axis
        if max_dim_index == 0:
            obj.rotation_euler[1] = math.radians(90)
        # If the longest dimension was the Y-axis (index 1), rotate 90 degrees around the X-axis
        elif max_dim_index == 1:
            obj.rotation_euler[0] = math.radians(90)
        
    
    # Set the object's origin to its geometric center
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='BOUNDS')

    # Set the object's location to the origin
    obj.location = (0, 0, 0)
    
    
       # Create a new material
    mat = bpy.data.materials.new(name="UserMaterial")
    # Ensure the material has a node tree
    if mat.node_tree is None:
        mat.use_nodes = True

    # Create a diffuse shader node
    diffuse_node = mat.node_tree.nodes.new('ShaderNodeBsdfDiffuse')
    diffuse_node.name = "Background"
    diffuse_node.inputs[0].default_value = (0, 0, 0, 1)  # RGBA for blue

    # Link the diffuse shader node to the material output
    output_node = mat.node_tree.nodes.get('Material Output')
    if output_node is not None:
        links = mat.node_tree.links
        links.new(diffuse_node.outputs['BSDF'], output_node.inputs['Surface'])

    # Assign the material to the object
    if len(obj.data.materials):
        # If the object already has a material, replace it
        obj.data.materials[0] = mat
    else:
        # Otherwise, add the new material
        obj.data.materials.append(mat)
    
    # Check if there is a light in the scene
    light_exists = any(obj for obj in bpy.data.objects if obj.type == 'LIGHT')

    # If not, add a light
    if not light_exists:
        # Add a new sun light
        bpy.ops.object.light_add(type='SUN', location=(obj.location.x, obj.location.y, obj.location.z + 50))
    # Check if the 'Empty' object exists
    if 'Empty' not in bpy.data.objects:
        # If it doesn't exist, add an empty object of type 'SPHERE'
        bpy.ops.object.empty_add(type='SPHERE')
    # Check if there is a camera in the scene
    camera_exists = any(obj for obj in bpy.data.objects if obj.type == 'CAMERA')    

    if not camera_exists:
        # Add a new camera
        bpy.ops.object.camera_add(location=(x, y, z))

        # Get the newly added camera
        camera = bpy.context.object

        # Select the camera
    cam = bpy.data.objects['Camera']  # Replace with your camera's name

    # Position the camera above the object
    cam.location = (obj.location.x, obj.location.y, obj.location.z + max_dim * 2)
    cam.data.type = 'ORTHO'
    cam.data.ortho_scale = max_dim * 2
    # Set the active camera
    bpy.context.scene.camera = cam
    # Point the camera downwards
    cam.rotation_euler = (math.radians(0), 0, 0) 
    # Set World background to white
    bpy.data.worlds['World'].node_tree.nodes['Background'].inputs['Color'].default_value = (1, 1, 1, 1)  # RGBA for white

        
    # Get the empty object
    empty = bpy.data.objects['Empty']

    # Get the constraint
    rot_constraint = obj.constraints.get('COPY_ROTATION')

    # If the constraint doesn't exist, create it
    if rot_constraint is None:
        rot_constraint = obj.constraints.new('COPY_ROTATION')

    # Set target object to the empty object
    rot_constraint.target = empty 

    # Set rotation axis
    rot_constraint.use_x = False
    rot_constraint.use_y = True
    rot_constraint.use_z = True

    # Set owner to local space
    rot_constraint.owner_space = 'LOCAL'

    
     
    if not os.path.exists(render_output_directory):
        os.makedirs(render_output_directory)
    # Set the resolution
    bpy.context.scene.render.resolution_x = 1000
    bpy.context.scene.render.resolution_y = 1000
    # Set render file format and output path
    bpy.context.scene.render.image_settings.file_format = 'JPEG'
    #bpy.context.scene.render.image_settings.color_mode = 'BW'
    
    # Initialize rotation angles
    foki = 0 # Rotation
    fokj = 0 # Tilt


    for j in range(num_rotations_fall+1):
        for i in range(num_rotations+1):
            # If the longest dimension was the x-axis (index 0)
            if max_dim_index == 0:
                obj.rotation_euler = (0, 0, math.radians(foki)) # Only rotate on the Z-axis
            # If the longest dimension was the Z-axis (index 2)    
            elif max_dim_index == 1:
                obj.rotation_euler = (0, math.radians(foki), 0)  # Only rotate on the Y-axis           
            # If the longest dimension was the Y-axis (index 1), rotate 90 degrees around the Y-axis
            elif max_dim_index == 2:
                obj.rotation_euler = (0, 0, math.radians(foki)) # Only rotate on the Z-axis

            #Store the file woth filename and rotation angle j and i     
            bpy.context.scene.render.filepath = os.path.join(render_output_directory, "{}_render_{:02d}_{:03d}.jpg".format(file_name,fokj, foki))
            bpy.ops.render.render(write_still=True)
            foki += rotation_increment
            #print(j,i)
        # Rotate the obj object after each full rotation of the empty object
        if max_dim_index == 0:    
            obj.rotation_euler[1] = math.radians(fokj)
        elif max_dim_index == 1:    
            obj.rotation_euler[1] = math.radians(fokj)
        if max_dim_index == 2:
            obj.rotation_euler[2] = math.radians(fokj)
        # If the longest dimension was the Y-axis (index 1), rotate 90 degrees around the X-axis
        

        fokj += rotation_increment_f
        foki = 0
    print("A kod lefutott rendben." ) # Maximum dimension of the object
