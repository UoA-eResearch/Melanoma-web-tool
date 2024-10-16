import json
import numpy as np
import trimesh
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

mesh_json = Path('./public/data/Heat_maps/Jsons_heat_maps_6-3-24/1_NFs_1.json')

with open(mesh_json) as f:
    data = json.load(f)

# Get the vertices and faces from the JSON file
verts = np.reshape(np.array(data['vertices']), (-1, 3))
faces = np.array(data['faces'])
clean_faces = np.reshape(clean_raw_faces(faces), (-1,3))
normals = np.reshape(np.array(data['normals']), (-1,3))

mesh_json = {'name': 'human_mesh', 'vertices': verts.tolist(), 'faces': clean_faces.tolist(), 'normals': normals.tolist()}
json.dump(mesh_json, open("human_mesh.json", 'w'))

mesh = trimesh.Trimesh(vertices=verts, faces=clean_faces, normals=normals)
mesh.export('./human_mesh.obj')