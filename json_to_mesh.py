import os
import numpy as np
import json
import trimesh
import pandas as pd
from tqdm import tqdm
from pathlib import Path

# Function to clean and reshape raw face data into standard x,y,z format
def clean_raw_faces(faces):
    temp = []
    face_id = 0
    for i in faces:
        if face_id == 0:
            face_id = i
            continue
        if face_id != 0 and i == face_id:
            continue
        else:
            temp.append(i)
    
    reshaped = np.reshape(np.array(temp), (-1,3))
    uniq_faces = np.unique(reshaped, axis = 0)
    face_data = uniq_faces

    return np.array(face_data)

if __name__ == "__main__":
    mesh_json = Path('./public/data/all_element_jasons/element_all.json')
    stats_json = Path('./src/data/data_elements.json')
    mesh_elements_json_dir = Path('./public/data/all_element_jasons/')

    # Arrays to store mesh element data
    verts = []
    faces = []
    verts_normals = []
    element_data_list = []
    stats = []
    mesh_list = []
    fnames = []
    stats_rows = []


    # Load the mesh json file
    with open(mesh_json) as f:
        mesh_data = json.load(f)

        # Get group names for each mesh element
        for row in mesh_data:
            try:
                element_data_list.append([row['URL'], row['GroupName']])
            except:
                continue

    # load in stats data
    with open(stats_json) as f:
        stats_data = json.load(f)

    # Iterate through the json file and extract the individual json files
    files_list = []
    skip_files = ['Nodes/all_nodes_labels_2.json', 'skin_cancer_Layout_view.json']
    for idx, row in enumerate(mesh_data):
        keys = mesh_data[idx]['URL']
        if 'Lines' in keys:
            continue
        if keys in skip_files:
            print('[Info] Skipping file: ', keys)
            continue

        files_list.append(keys)

    for file in tqdm(files_list):
        print("[Info] Processing file...: ", file)
        # load the json file for processing
        with open(Path.joinpath(mesh_elements_json_dir, Path(file))) as f:
            data = json.load(f)

        if type(data) is list:
            continue

        if 'vertices' not in data:
            continue
        
        # Extract the vertices, faces and normals data
        raw_faces = np.array(data['faces'])
        # Clean the raw faces data
        cleaned_faces = clean_raw_faces(raw_faces)
        faces.append(cleaned_faces) 

        try:
            verts_reshaped = np.reshape(np.array(data['vertices']), (-1,3))
            verts_normals_reshaped = np.reshape(np.array(data['normals']), (-1,3))
        except:
            raise ValueError('Error in reshaping vertices and normals data')

        verts.append(verts_reshaped)
        verts_normals.append(verts_normals_reshaped)

        mesh_elements_arr = np.array(element_data_list)[:,0].tolist()
        Gname = element_data_list[mesh_elements_arr.index(file)][1]
        try:
            stats_data_row = stats_data[Gname]
        except:
            stats_data_row = ['Data not available']

        extras = {"json_filename" : file} 
        mesh = trimesh.Trimesh(vertices=verts_reshaped, faces=cleaned_faces, vertex_normals=verts_normals_reshaped, 
                               extras=extras, metadata=extras, process=False)

        fnames.append(file)
        fname = file.strip('.json')
        splits = fname.split('/')
        fname = splits[0] + '-' + splits[1] + '.obj'
        stats_rows.append(stats_data_row)
        mesh_list.append(mesh)
        # Optional: Save individual meshes to a new obj/ply etc file
        # mesh.export(fname)

# Combine all the mesh elements into a single mesh and apply a scale factor
combined_mesh = trimesh.util.concatenate(mesh_list)
# Scale the mesh (1 unit here)
scale_factor = 1.0 / combined_mesh.bounding_box.extents.max()
combined_mesh.apply_scale(scale_factor)

#Optional: Save the combined mesh to a new obj/ply etc file
combined_mesh.export('combined_mesh.obj')

for idx, mesh in enumerate(mesh_list):
    mesh.apply_scale(scale_factor)
    # Get the xyz min and max bounds for each mesh element
    bnds = mesh.bounds
    json_obj = {}
    json_obj['json_filename'] = fnames[idx] + '.json'
    json_obj['bounds'] = bnds.tolist()
    json_obj['stats_data'] = stats_rows[idx]
    stats.append(json_obj)

json.dump(stats, open("stats_data.json", 'w'))



    




