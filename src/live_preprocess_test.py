import cv2
import numpy as np

from camera import open_camera, read_frame, release_camera


PHONE_CAMERA_URL = "http://192.168.7.2:8080/video"


def prepare_frame(frame):
    """Prepare a live camera frame for the AI model."""

    # Resize to the model input size
    resized = cv2.resize(frame, (160, 160))

    # Convert pixel values from 0-255 to 0-1
    normalized = resized.astype(np.float32) / 255.0

    return resized, normalized


def main():
    camera = open_camera(PHONE_CAMERA_URL)

    print("Live preprocessing started.")
    print("Press Q to quit.")

    while True:
        frame = read_frame(camera)

        resized, normalized = prepare_frame(frame)

        # Display the resized image
        cv2.imshow("CropDoc AI - 160x160 Input", resized)

        # Print information once every frame for now
        print(
            f"Shape: {normalized.shape} | "
            f"Dtype: {normalized.dtype} | "
            f"Range: {normalized.min():.2f}-{normalized.max():.2f}",
            end="\r"
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    release_camera(camera)
    print("\nPreprocessing stopped.")


if __name__ == "__main__":
    main()