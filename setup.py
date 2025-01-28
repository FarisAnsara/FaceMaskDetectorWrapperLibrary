from setuptools import setup, find_packages

setup(
    name="face_mask_wrapper",
    version="1.0",
    description="A Python library for detecting whether a person is wearing a mask using a pre-trained CNN model.",
    author="Faris Ansara", 
    author_email="faris.ansara@gmail.com",
    url="https://github.com/FarisAnsara/FaceMaskDetectorWrapperLibrary",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "tensorflow",
        "numpy",
        "pillow"
    ],
    package_data={
        "mask_detector": ["mask_detector_model.h5"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
