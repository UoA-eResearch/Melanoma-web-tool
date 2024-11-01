import numpy as np
import json
from tqdm import tqdm
from pathlib import Path

processed_data = []
lymphs_json = Path('./public/data/all_element_jasons/Nodes/all_nodes_labels_2.json')

if __name__ == "__main__":
    #load in lymph json data
    with open(lymphs_json) as f:
        lymphs_data = json.load(f)

    pts = lymphs_data['positions']
    lbls = lymphs_data['label']

    #reshape points to xyz co-ordinates
    pts = np.reshape(pts['0'], (-1, 3))
    print(len(lbls))
    assert pts.shape[0] == len(lbls)

    for idx in tqdm(range(pts.shape[0])):
        processed_data.append({'label': lbls[idx], 'position': pts[idx].tolist()})

    json.dump(processed_data, open("lymphs_positions.json", 'w'))
    





    