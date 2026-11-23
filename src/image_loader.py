import cv2
import numpy as np

class ImageLoader:
    
    def load(self, path: str) -> np.ndarray:
        image = cv2.imread(path)

        if image is None:
            raise FileNotFoundError(f"Image not found at path: {path}")
        
        return image

    def load_bytes(self,image_bytes: bytes) -> np.ndarray:

        array = np.frombuffer(
            image_bytes,
            dtype=np.uint8
        )

        image = cv2.imdecode(
            array,
            cv2.IMREAD_COLOR
        )

        if image is None:
            raise ValueError(
                "could not decode image"
            )

        return image
    