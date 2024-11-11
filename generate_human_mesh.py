import json
import numpy as np
import trimesh
from pathlib import Path

mesh_json = Path('./public/data/Heat_maps/Jsons_heat_maps_6-3-24/1_NFs_1.json')

with open(mesh_json) as f:
    data = json.load(f)

verts = np.reshape(data['vertices'], (-1, 3))
print(verts.shape)
print(np.unique(verts, axis=0).shape)
faces = np.reshape(data["faces"], (-1,10))
faces = faces[:,1:4]
print(faces.shape)

# process=False is needed here to prevent merging vertices, which throws off the heatmaps
mesh = trimesh.Trimesh(vertices=verts, faces=faces, process=False)
mesh.export('./human_mesh.glb')