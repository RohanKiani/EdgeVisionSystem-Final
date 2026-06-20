try:
    import cv2
except ImportError as e:
    raise ImportError("OpenCV is required. Install with `pip install opencv-python`.") from e
import time

from logger import log_detections
from camera import get_camera
from detector import detect
from logger import log_detections

cap = get_camera()

prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results, detections = detect(frame)

    annotated = results.plot()

    # FPS calculation
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time else 0
    prev_time = current_time

    cv2.putText(
        annotated,
        f"FPS: {int(fps)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    log_detections(detections)

    cv2.imshow("Edge Vision System", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()