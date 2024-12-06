#!/usr/bin/env python3
import os
import json
import numpy as np
import trimesh
from pathlib import Path
from tqdm import tqdm
import pandas as pd

heat_maps_verts_colors = {}
json_heatmaps_dir = './public/data/'

with open("public/data/heat_maps.json") as f:
    elems = json.load(f)

discrete_points_normalized = {}

for elem in tqdm(elems):
    try:
        if elem["Type"] == "Surfaces":
            name = elem.get("RegionPath", "") + " " + elem.get("GroupName", "")
            name = name.replace("Heat Map", "").strip()
            file = json_heatmaps_dir + elem["URL"]
            with open(file) as f:
                data = json.load(f)
                heat_maps_verts_colors[name] = data['colors']
        elif elem["Type"] == "Glyph":
            RegionPath = elem.get("RegionPath", "")
            file = json_heatmaps_dir + elem["URL"]
            if "fre" in file:
                RegionPath += " Frequency"
                #print(RegionPath)
            with open(file) as f:
                data = json.load(f)
                pos = np.reshape(data["positions"]["0"], (-1, 3)).tolist()
                #scale = np.reshape(data["scale"]["0"], (-1, 3))
                #scale = scale[:,1].tolist()
                if RegionPath in discrete_points_normalized:
                    print(f"Duplicate {RegionPath}")
                discrete_points_normalized[RegionPath] = {
                    "positions": pos,
                    "colors": data["colors"]["0"],
                    #"scales": scale,
                }
            file = os.path.basename(file)
            file = "public/data/Heat_maps/discrete_points_normalized/" + file.replace("nor", "fre").replace("_points", "").replace("_pointys", "").replace("NFs", "NFS")
            if os.path.isfile(file) and "fre" in file and "Frequency" not in RegionPath:
                RegionPath += " Frequency"
                #print(RegionPath)
                with open(file) as f:
                    data = json.load(f)
                    pos = np.reshape(data["positions"]["0"], (-1, 3)).tolist()
                    #scale = np.reshape(data["scale"]["0"], (-1, 3))
                    #scale = scale[:,1].tolist()
                    if RegionPath in discrete_points_normalized:
                        print(f"Duplicate {RegionPath}")
                    discrete_points_normalized[RegionPath] = {
                        "positions": pos,
                        "colors": data["colors"]["0"],
                        #"scales": scale,
                    }
    except Exception as e:
        print(f"{e} for {elem}")
        raise

json.dump(heat_maps_verts_colors, open("heat_maps_verts_colors.json", 'w'))

for k in discrete_points_normalized:
    if "Frequency" in k:
        print(k)

json.dump(discrete_points_normalized, open("discrete_points_normalized.json", 'w'))