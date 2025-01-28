from .MaskDetector import MaskDetector
import os

class MaskDetectorWrapper:
    def __init__(self):
        """
        Wrapper class for the MaskDetector library.
        :param model_path: Path to the pre-trained model file.
        """
        self.detector = MaskDetector()

    def predict(self, image_path):
        """
        Predict whether the person in the image is wearing a mask or not.
        :param image_path: Path to the image file.
        :return: "With Mask" or "Without Mask"
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found at: {image_path}")
        
        try:
            result = self.detector.predict(image_path)
            return result
        except Exception as e:
            raise RuntimeError(f"Error during prediction: {str(e)}")
