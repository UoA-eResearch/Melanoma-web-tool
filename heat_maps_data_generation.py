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
            if "fre" in file and "Frequency" not in RegionPath:
                RegionPath += " Frequency"
                #print(RegionPath)
            if RegionPath not in discrete_points_normalized:
                with open(file) as f:
                    data = json.load(f)
                    pos = np.reshape(data["positions"]["0"], (-1, 3)).tolist()
                    #scale = np.reshape(data["scale"]["0"], (-1, 3))
                    #scale = scale[:,1].tolist()
                    discrete_points_normalized[RegionPath] = {
                        "positions": pos,
                        "colors": data["colors"]["0"],
                        #"scales": scale,
                    }
            file = os.path.basename(file)
            file = "public/data/Heat_maps/discrete_points_frequency/" + file.replace("nor", "fre").replace("_points", "_fre_points").replace("_pointys", "").replace("NFs", "NFS").replace("_fre_fre", "_fre")
            if not os.path.isfile(file):
                file = file.replace("_fre_points", "_fre")
            #print(file, os.path.isfile(file), RegionPath)
            if os.path.isfile(file) and "fre" in file and "Frequency" not in RegionPath:
                RegionPath += " Frequency"
                #print(RegionPath)
                if RegionPath not in discrete_points_normalized:
                    with open(file) as f:
                        data = json.load(f)
                        pos = np.reshape(data["positions"]["0"], (-1, 3)).tolist()
                        #scale = np.reshape(data["scale"]["0"], (-1, 3))
                        #scale = scale[:,1].tolist()
                        discrete_points_normalized[RegionPath] = {
                            "positions": pos,
                            "colors": data["colors"]["0"],
                            #"scales": scale,
                        }
    except Exception as e:
        print(f"{e} for {elem}")
        #raise

for code in tqdm(["Liei", "Lif", "Lii", "Laa", "Lam", "Lap", "Riei", "Rif", "Rii", "Raa", "Ram", "Rap"]):
    if code[0:2] == "Li":
        RegionPath = "Left Groin/Sub-Node Fields " + code
    elif code[0:2] == "Ri":
        RegionPath = "Right Groin/Sub-Node Fields " + code
    elif code[0:2] == "La":
        RegionPath = "Left Axilla/Sub-Node Fields " + code
    elif code[0:2] == "Ra":
        RegionPath = "Right Axilla/Sub-Node Fields " + code
    else:
        raise ValueError(f"Unknown code {code}")
    file = f"public/data/Heat_maps/Sub_fields/{code.lower()}_points_2.json"
    try:
        with open(file) as f:
            data = json.load(f)
            pos = np.reshape(data["positions"]["0"], (-1, 3)).tolist()
            discrete_points_normalized[RegionPath] = {
                "positions": pos,
                "colors": data["colors"]["0"],
            }
    except Exception as e:
        print(e)
    file = f"public/data/Heat_maps/discrete_points_frequency/{code.lower()}_fre_points_2.json"
    RegionPath += " Frequency"
    try:
        with open(file) as f:
            data = json.load(f)
            pos = np.reshape(data["positions"]["0"], (-1, 3)).tolist()
            discrete_points_normalized[RegionPath] = {
                "positions": pos,
                "colors": data["colors"]["0"],
            }
    except Exception as e:
        print(e)

print(f"Number of heatmaps: {len(heat_maps_verts_colors)}")
json.dump(heat_maps_verts_colors, open("heat_maps_verts_colors.json", 'w'))

nf = sum("Frequency" in k for k in discrete_points_normalized)
print(f"Number of frequency discrete points: {nf}/{len(discrete_points_normalized)}")

json.dump(discrete_points_normalized, open("discrete_points_normalized.json", 'w'))

print(sorted(discrete_points_normalized.keys()))
for k in heat_maps_verts_colors:
    if k not in discrete_points_normalized:
        print(f"Missing normalised for {k}")
    if k + " Frequency" not in discrete_points_normalized:
        print(f"Missing frequency for {k}")