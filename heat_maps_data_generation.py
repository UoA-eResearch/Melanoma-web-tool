import os
import json
import numpy as np
import trimesh
from pathlib import Path
from tqdm import tqdm

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

def rgb_int2tuple(idx, rgbint):
    return (int(rgbint // 256 // 256 % 256), int(rgbint // 256 % 256), int(rgbint % 256), int(idx))

if __name__ == "__main__":
    heat_maps_verts_colors = []
    json_heatmaps_dir = Path('./public/data/Heat_maps/')

    for file in tqdm(os.listdir(json_heatmaps_dir)):
        if not file.endswith('.json'):
            continue

        with open(Path.joinpath(json_heatmaps_dir, file)) as f:
            data = json.load(f)
            raw_colors = np.array(data['colors'])
            
            rgb = []
            for i,c in enumerate(raw_colors):
                RGB = rgb_int2tuple(1, c)
                rgb.append(RGB)
            
            heat_maps_verts_colors.append({'name':file, 'heatmap':rgb})
    
    # Not all jsons are in the same directory
    for file in os.listdir(Path.joinpath(json_heatmaps_dir, 'Jsons_heat_maps_6-3-24')):
        if not file.endswith('.json'):
            continue

        with open(Path.joinpath(json_heatmaps_dir, 'Jsons_heat_maps_6-3-24', file)) as f:
            data = json.load(f)
            raw_colors = np.array(data['colors'])
            
            rgb = []
            for i,c in enumerate(raw_colors):
                RGB = rgb_int2tuple(1, c)
                rgb.append(RGB)
            
            heat_maps_verts_colors.append({'name':file, 'heatmap':rgb})

    json.dump(heat_maps_verts_colors, open("heat_maps_verts_colors.json", 'w'))
