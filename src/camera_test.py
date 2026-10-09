import cv2
from camera import open_camera, read_frame, release_camera


PHONE_CAMERA_URL = "http://192.168.7.2:8080/video"


def main():
    camera = open_camera(PHONE_CAMERA_URL)

    print("Phone camera connected.")
    print("Press Q to quit.")

    while True:
        frame = read_frame(camera)

        cv2.imshow("CropDoc AI - Phone Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    release_camera(camera)
    print("Camera released.")


if __name__ == "__main__":
    main()