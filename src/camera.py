import cv2
from config import CAMERA_INDEX, FRAME_WIDTH, FRAME_HEIGHT


def get_camera():

    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    if not cap.isOpened():
        raise Exception("Camera not accessible")

    return cap