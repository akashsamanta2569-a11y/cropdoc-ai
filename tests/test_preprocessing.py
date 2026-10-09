import cv2
from src.preprocessing import prepare_image


def test_prepare_image():
    image = cv2.imread("data/test_leaf.jpg")

    assert image is not None, "Test image could not be loaded."

    processed = prepare_image(image)

    assert processed.shape == (224, 224, 3)
    assert processed.dtype == "float32"
    assert processed.min() >= 0.0
    assert processed.max() <= 1.0

    print("Preprocessing test passed.")


if __name__ == "__main__":
    test_prepare_image()