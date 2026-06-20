import json
import os
import time

LOG_FILE = "outputs/detections.json"


def log_detections(detections):

    os.makedirs("outputs", exist_ok=True)

    entry = {
        "timestamp": time.time(),
        "detections": detections
    }

    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                data = json.load(f)
        except:
            data = []
    else:
        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)