#!/usr/bin/env python3
import numpy as np
import json
import trimesh
from tqdm import tqdm
from pathlib import Path
import pandas as pd

df = pd.read_json('./public/data/all_element_jasons/element_all.json').drop_duplicates()
df = df[df.Type.isin(["Surfaces", "Lines"])]
mesh_elements_json_dir = Path('./public/data/all_element_jasons/')
scene = trimesh.scene.Scene()

for row in tqdm(df.itertuples(index=False), total=df.shape[0]):
    file = row.URL
    #print(file)
    GroupName = row.GroupName
            
    with open(Path.joinpath(mesh_elements_json_dir, Path(file))) as f:
        data = json.load(f)
    
    if type(data) is list:
        print(f"Skipping {file}, data is a list")
        continue

    if 'vertices' not in data:
        print(f"Skipping {file}, vertices not found")
        continue

    try:
        verts_reshaped = np.reshape(data['vertices'], (-1,3))
        #verts_normals_reshaped = np.reshape(data['normals'], (-1,3))
        if data["faces"][0] == 32:
            faces_reshaped = np.reshape(data["faces"], (-1,7))
        elif data["faces"][0] == 40:
            faces_reshaped = np.reshape(data["faces"], (-1,10))
        elif data["faces"][0] == 0:
            faces_reshaped = np.reshape(data["faces"], (-1,4))
        else:
            raise ValueError(f'Error in reshaping faces data {file}')
        faces_reshaped = faces_reshaped[:,1:4]
    except:
        raise ValueError(f'Error in reshaping vertices and normals data {file}')

    mesh = trimesh.Trimesh(vertices=verts_reshaped, faces=faces_reshaped)
    scene.add_geometry(mesh, geom_name=GroupName)

scene.export('./scene.obj')
