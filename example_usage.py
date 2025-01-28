from mask_detector import MaskDetectorWrapper
import os

wrapper = MaskDetectorWrapper()

image_path = os.path.join('test_image', 'with_mask_5.jpg')
result = wrapper.predict(image_path)

print(f"Prediction for {image_path}: {result}")
