import cv2
import numpy as np

class ImageLoader:
    def load(self, path: str) -> np.ndarray:
        image = cv2.imread(path)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {path}")
        return image