import os
import json


def export(metrics_data):
    old_file_content = {"metrics": []}
    if os.path.exists("metrics.json"):
        with open("metrics.json") as f:
            old_file_content = json.load(f)

    old_file_content["metrics"].append(metrics_data)
    with open("metrics.json", "w") as f:
        json.dump(old_file_content, f, indent=4, default=str)
