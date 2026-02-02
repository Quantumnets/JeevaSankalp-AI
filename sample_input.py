import json

sample_data = {
    "land_id": "LS-001",
    "soil_ph": 6.5,
    "organic_carbon": 0.82,
    "moisture": 23,
    "nitrogen": 45,
    "previous_crop": "millet"
}

with open("data/input.json", "w") as f:
    json.dump(sample_data, f, indent=4)

print("Sample input data created.")