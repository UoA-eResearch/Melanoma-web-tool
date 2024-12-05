#!/usr/bin/env python3
import os
import json
import numpy as np
import trimesh
from pathlib import Path
from tqdm import tqdm
import pandas as pd

heat_maps_verts_colors = {}
json_heatmaps_dir = Path('./public/data/')

with open("public/data/heat_maps.json") as f:
    elems = json.load(f)

discrete_points_normalized = {}

for elem in tqdm(elems):
    try:
        if elem["Type"] == "Surfaces":
            name = elem.get("RegionPath", "") + " " + elem.get("GroupName", "")
            name = name.replace("Heat Map", "").strip()
            file = elem["URL"]
            with open(Path.joinpath(json_heatmaps_dir, file)) as f:
                data = json.load(f)
                heat_maps_verts_colors[name] = data['colors']
        elif elem["Type"] == "Glyph":
            RegionPath = elem.get("RegionPath", "")
            file = elem["URL"]
            if "fre" in file:
                RegionPath += " Frequency"
            with open(Path.joinpath(json_heatmaps_dir, file)) as f:
                data = json.load(f)
                pos = np.reshape(data["positions"]["0"], (-1, 3)).tolist()
                scale = np.reshape(data["scale"]["0"], (-1, 3))
                scale = scale[:,1].tolist()
                if RegionPath in discrete_points_normalized:
                    print(f"Duplicate {RegionPath}")
                discrete_points_normalized[RegionPath] = {
                    "positions": pos,
                    "colors": data["colors"]["0"],
                    #"scales": scale,
                }
    except Exception as e:
        print(f"{e} for {elem}")

json.dump(heat_maps_verts_colors, open("heat_maps_verts_colors.json", 'w'))
json.dump(discrete_points_normalized, open("discrete_points_normalized.json", 'w'))