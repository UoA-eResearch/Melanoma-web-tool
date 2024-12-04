#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv("public/data/All_patient_data_fre/element_patient_counts.csv")
df["Element #"] = df["Element #"].astype(int)
df.set_index("Element #", inplace=True)
df["Number of Patients"].to_json("element_patient_counts.json")