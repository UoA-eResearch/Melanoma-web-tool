# Melanoma web tool

### Installation

Install Python, then run `pip install -r requirements.txt` to install the required packages.

### Running

If necessary, you can run the below scripts to generate these outputs:

Skin selection tool:

- Run `json_to_mesh.py` to build `scene.glb` from `public/data/all_element_jasons/element_all.json`. This will stitch all elements together, while preserving their element names.
- Run `lymph_positional_data.py` to parse `public/data/all_element_jasons/Nodes/all_nodes_labels_2.json` and generate `lymphs_positions.json`, a json file containing the lymph positions inside the human body
- Run `parse_patient_counts.ipynb` to parse `public/data/All_patient_data_fre/element_patient_counts.csv` and `public/data/All_patient_data_fre/Readme_element_grouping.txt` to then generate `element_patient_counts.json`, a json file containing the patient counts for each element

Heatmap tool:

- Run `generate_human_mesh.py` to generate `human_mesh.glb`, a combined human mesh. This reads the mesh information from `public/data/Heat_maps/Jsons_heat_maps_6-3-24/1_NFs_1.json`, but any of the JSON heatmaps will work fine as they all include the same mesh information.
- Run `heat_maps_data_generation.py` to parse `public/data/heat_maps.json` and output `heat_maps_verts_colors.json` and `discrete_points_normalized.json`. `heat_maps_verts_colors.json` contains all the different heatmaps as vertex colors for `human_mesh.glb`. `discrete_points_normalized.json` contains the discrete points for the heatmap.

## About the Three.js web tool

To view `index.html` locally, you can use `python -m http.server` in the root directory and navigate to `localhost:8000` in your browser. Alternatively, you can use the `Live Server` extension in Visual Studio Code.

`index.html` depends only on the following files:

- scene.glb
- lymphs_positions.json
- human_mesh.glb
- heat_maps_verts_colors.json
- discrete_points_normalized.json
- src/data/data_elements.json
- element_patient_counts.json