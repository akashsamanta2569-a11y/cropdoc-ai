import cv2
from camera import open_camera, read_frame, release_camera


PHONE_CAMERA_URL = "http://192.168.7.22:8080/video"


def main():
    camera = open_camera(PHONE_CAMERA_URL)

    print("Camera connected.")
    print("Press SPACE to capture an image.")
    print("Press Q to quit.")

    while True:
        frame = read_frame(camera)

        cv2.imshow("CropDoc AI - Capture Test", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord(" "):
            cv2.imwrite("../data/test_leaf.jpg", frame)
            print("Image saved: ../data/test_leaf.jpg")
            break

        if key == ord("q"):
            break

    release_camera(camera)


if __name__ == "__main__":
    main()