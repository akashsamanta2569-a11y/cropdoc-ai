import cv2


def open_camera(source=0):
    """Open a local camera or network camera stream."""
    camera = cv2.VideoCapture(source)

    if not camera.isOpened():
        raise RuntimeError(f"Could not open camera source: {source}")

    return camera


def read_frame(camera):
    """Read one frame from the camera."""
    success, frame = camera.read()

    if not success:
        raise RuntimeError("Could not read frame from camera.")

    return frame


def release_camera(camera):
    """Release the camera safely."""
    camera.release()
    cv2.destroyAllWindows()