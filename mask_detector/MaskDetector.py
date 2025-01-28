import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

class MaskDetector:
    def __init__(self, model_path='mask_detector_model.h5'):
        """
        Initialize the MaskDetector class.
        :param model_path: Path to the trained model (.h5 file).
        """
        default_model_path = os.path.join(os.path.dirname(__file__), model_path)
        self.load_model(default_model_path)

    def load_model(self, model_path):
        """
        Load the trained model.
        :param model_path: Path to the trained model (.h5 file).
        """
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at: {model_path}")
        self.model = tf.keras.models.load_model(model_path)
        print("Model loaded successfully")

    def preprocess_image(self, image_path, target_size=(128, 128)):
        """
        Preprocess the image to prepare it for prediction.
        :param image_path: Path to the image file.
        :param target_size: Target size for resizing the image.
        :return: Preprocessed image as a NumPy array.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found at: {image_path}")
        image = load_img(image_path, target_size=target_size)
        image_array = img_to_array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        return image_array

    def predict(self, image_path):
        """
        Predict if the person in the image is wearing a mask.
        :param image_path: Path to the image file.
        :return: "With Mask" or "Without Mask"
        """
        if not self.model:
            raise ValueError("Model is not loaded. Use `load_model` to load a model first.")
        
        processed_image = self.preprocess_image(image_path)
        prediction = self.model.predict(processed_image)[0][0]
        return "Without Mask" if prediction > 0.5 else "With Mask"
