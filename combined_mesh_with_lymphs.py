import numpy as np
import json
import trimesh
from pathlib import Path

# Arrays to store mesh element data
translated_lymphs = []

#Hard coded to match the mesh and lymphs
scaling_factor = 0.90 
translation_vector = [28, 11, -3]

#lymph data path
lymph_positional_json = Path('./lymphs_positions.json')
combined_mesh_path = Path('./human_mesh.obj')

# Function to create a lymph mesh at a given location
def create_lymph(idx, center, radius):
    #center = np.multiply(center , translation_vector)
    lymph = trimesh.creation.icosphere(subdivisions=2, radius=radius)
    lymph.apply_translation(center)  # Move the lymph to the vertex location
    return lymph

if __name__ == "__main__":
    lymph_bounds_data = []
    mesh = trimesh.load_mesh(combined_mesh_path)
    
    # make mesh transparent for easier viewing of lymph nodes and mesh
    # Set opacity to x% (which means at 10% opacity, alpha = 0.1)
    opacity = 0.7  #1 = transparent, 0 = opaque
    alpha_value = int(255 * (1 - opacity))  # Calculate the alpha value

    # Create vertex colors with white color and the specified alpha
    mesh.visual.vertex_colors = np.array([[255, 255, 255, alpha_value]] * len(mesh.vertices))

    # Check if the mesh has the visual attribute
    if not hasattr(mesh.visual, 'vertex_colors'):
        mesh.visual.vertex_colors = np.zeros((len(mesh.vertices), 4), dtype=np.uint8)
        mesh.visual.vertex_colors[:, 3] = alpha_value  # Set alpha for all vertices

    # Verify that the mesh is valid
    if mesh.is_empty:
        print("Error: The original mesh is empty or invalid.")
    else:
        print(f"Original mesh has {len(mesh.vertices)} vertices and {len(mesh.faces)} faces.")

    # Load the lymph nodes data
    # Get vertices (XYZ points)
    with open(lymph_positional_json) as f:
        lymph_data = json.load(f)
    
    lymph_pos = []
    lymph_lbl = []
    for row in lymph_data:
        lymph_pos.append(row['position'])
        lymph_lbl.append(row['label'])

    # Create lymphs at each vertex location
    lymphs = []
    radius = 7  # Adjust based on requirements

    # Create a lymph for each vertex and store them in the list
    for idx, point in enumerate(lymph_pos):
        lymph = create_lymph(idx, point, radius)
        lymphs.append(lymph)

    for idx, lymph in enumerate(lymphs):
        translated_lymphs.append(lymph.apply_translation(translation_vector).apply_scale(scaling_factor))
        lymph_name = lymph_lbl[idx]
        lymph_bounds_data.append({'name': lymph_name, 'bounds': lymph.bounds.tolist()})

    # Bounds and name of the lymph node to be used in the web app
    json.dump(lymph_data, open('./lymphs_bounds.json', 'w'))

    # Combine all lymphs into a single mesh
    combined_lymphs_mesh = trimesh.util.concatenate(translated_lymphs)
    
    #Optional: Save the combined lymphs mesh to a new obj/ply etc file
    combined_lymphs_mesh.export('./combined_lymphs.obj')

    #Adjust based on visual preference for testing
    # Set opacity to 10% (which means alpha = 0.1)
    opacity = 0.1  # 10% opaque
    alpha_value = int(255 * (1 - opacity))  # Calculate the alpha value

    # Create vertex colors with white color and the specified alpha
    combined_lymphs_mesh.visual.vertex_colors = np.array([[255, 0, 0, alpha_value]] * len(combined_lymphs_mesh.vertices))

    # Check if the mesh has the visual attribute
    if not hasattr(combined_lymphs_mesh.visual, 'vertex_colors'):
        combined_lymphs_mesh.visual.vertex_colors = np.zeros((len(combined_lymphs_mesh.vertices), 4), dtype=np.uint8)
        combined_lymphs_mesh.visual.vertex_colors[:, 3] = alpha_value  # Set alpha for all vertices

    # Combine the original mesh and the translated lymphs
    combined_mesh = trimesh.util.concatenate([mesh, combined_lymphs_mesh])

    # Now concatenate the original mesh and the scaled lymphs
    combined_mesh = trimesh.util.concatenate([mesh, combined_lymphs_mesh])
    combined_mesh.show()

    print("Original mesh bounds:", mesh.bounds)
    print("Lymphs mesh bounds:", combined_lymphs_mesh.bounds)
    print("New combined mesh bounds:", combined_mesh.bounds)

    # Export combined mesh with lymphs to a new obj file
    combined_mesh.export('combined_mesh_with_lymphs.obj')
    print("Combined mesh exported")






