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

for elem in tqdm(elems):
    if elem["Type"] == "Surfaces":
        name = elem.get("RegionPath", "") + " " + elem.get("GroupName", "")
        name = name.replace("Heat Map", "").strip()
        file = elem["URL"]
        with open(Path.joinpath(json_heatmaps_dir, file)) as f:
            data = json.load(f)
            heat_maps_verts_colors[name] = data['colors']

json.dump(heat_maps_verts_colors, open("heat_maps_verts_colors.json", 'w'))
