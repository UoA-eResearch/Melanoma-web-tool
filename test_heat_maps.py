import trimesh
import numpy as np
import json
from tqdm import tqdm
from pathlib import Path

#exports all the heatmaps as obj files separately
with open(Path('./human_mesh.json')) as f:
    mesh_data = json.load(f)

with open(Path('./heat_maps_verts_colors.json')) as f:
    colors = json.load(f)

for i in tqdm(range(len(colors))):
    color_data = colors[i]['heatmap']
    name = colors[i]['name'].strip('.json')

    new_mesh = trimesh.Trimesh(vertices=mesh_data['vertices'], faces=mesh_data['faces'], vertex_normals=mesh_data['normals'], vertex_colors=color_data)
    new_mesh.export(Path('./heatmap_' / name / '.obj'))