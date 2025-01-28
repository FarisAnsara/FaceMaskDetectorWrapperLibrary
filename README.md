# Face Mask Wrapper Library

## Overview
The `Face Mask Wrapper Library` provides a simple interface for detecting whether a person in an image is wearing a mask using a pre-trained CNN model. The library handles model loading, preprocessing, and inference, making it user-friendly and efficient.

---

## Installation

### 1. **Clone the Repository**
First, clone the repository to your local machine:
```bash
git clone https://github.com/FarisAnsara/FaceMaskDetectionWrapper.git
```
Navigate to the cloned directory:
```bash
cd FaceMaskDetectionWrapper
```

### 2. **Install the Library**
To install the library locally, navigate to the root directory of the project (where `setup.py` is located) and run:
```bash
pip install .
```

This will install the library on your system, allowing you to use it in any Python script.

---

## Requirements
- **Python Version**:
  - This library has been **tested** on Python **3.10**, **3.11**, and **3.12**.
  - It is also expected to be compatible with **Python 3.9** based on TensorFlow’s requirements.
  - Ensure you have Python 3.9 or higher installed for compatibility.

---

## Usage

### 1. **Importing the Library**
After installation, you can import the `MaskDetectorWrapper` class from the library:
```python
from mask_detector import MaskDetectorWrapper
```

---

### 2. **Creating an Instance of the Wrapper**
To use the wrapper, create an instance of the `MaskDetectorWrapper`:
```python
wrapper = MaskDetectorWrapper()
```
The wrapper automatically loads the pre-trained model from the package.

---

### 3. **Running Predictions**
Use the `predict` method to check if the person in the image is wearing a mask. Provide the path to the image file as the argument:
```python
image_path = "path/to/image.jpg"  # Replace with the actual image path
result = wrapper.predict(image_path)
print(f"Prediction for {image_path}: {result}")
```

---

## Expected Output
The `predict` method will return one of the following strings:
- **`"With Mask"`**: If the person in the image is wearing a mask.
- **`"Without Mask"`**: If the person in the image is not wearing a mask.

---

## Error Handling
The wrapper includes built-in error handling for common issues:
1. **FileNotFoundError**: Raised if the image file or model file does not exist.
   ```text
   FileNotFoundError: Image file not found at: <path>
   ```
2. **RuntimeError**: Raised if an error occurs during prediction.

---

## Notes
- Ensure the image file exists and is accessible at the specified path.
- The default model (`mask_detector_model.h5`) is included in the package and does not need to be downloaded separately.
