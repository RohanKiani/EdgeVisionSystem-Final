from ultralytics import YOLO
from config import MODEL_PATH, CONF_THRESHOLD

model = YOLO(MODEL_PATH)


def detect(frame):

    results = model(frame, verbose=False)[0]

    detections = []

    for box in results.boxes:

        conf = float(box.conf[0])

        if conf < CONF_THRESHOLD:
            continue

        cls = int(box.cls[0])
        label = model.names[cls]

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        detections.append({
            "label": label,
            "confidence": conf,
            "bbox": [x1, y1, x2, y2]
        })

    return results, detections