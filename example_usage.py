from mask_detector import MaskDetector

detector = MaskDetector()

image_path = "test_image/with_mask_5.jpg"
result = detector.predict(image_path)

print(f"Prediction for {image_path}: {result}")
