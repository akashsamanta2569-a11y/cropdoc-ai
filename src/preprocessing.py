import cv2
import numpy as np


def resize_image(image, size=(224, 224)):
    """Resize an image to the requested width and height."""
    return cv2.resize(image, size)


def normalize_image(image):
    """Convert pixel values from 0-255 to 0-1."""
    return image.astype(np.float32) / 255.0


def prepare_image(image, size=(224, 224)):
    """Resize and normalize an image."""
    resized = resize_image(image, size)
    normalized = normalize_image(resized)

    return normalized