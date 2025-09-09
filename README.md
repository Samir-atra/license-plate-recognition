# License Plate Recognition

This repository contains two implementations of a License Plate Recognition (LPR) system. The first, `OldLPR(2018)`, is a traditional computer vision approach using OpenCV. The second, `LPR`, is a more modern approach using deep learning with TensorFlow and ImageAI.

## LPR (2023)

This is a more recent implementation of a license plate recognition system using modern deep learning techniques. It is built to be integrated into a camera system for real-time detection and classification of license plates.

### Technology Stack

*   **Python 3**
*   **TensorFlow/Keras**
*   **ImageAI:** A library for object detection and image classification.
*   **Jupyter Notebook:** The code is provided as a notebook for easy experimentation.
*   **OpenCV**
*   **Numpy**

### Methodology

The model consists of two main parts:

1.  **License Plate Detection:** A YOLOv3 object detection model, trained using the ImageAI library, is used to detect and locate license plates in an image.
2.  **Character Recognition:** A Recurrent Neural Network (RNN) is used to process the cropped license plate image as a time series of characters. This is an experimental approach to recognize the characters on the plate.

### Dataset

*   **License Plate Detection:** [Car Plate Detection dataset on Kaggle](https://www.kaggle.com/datasets/andrewmvd/car-plate-detection)
*   **Character Recognition:** [Characters Dataset for License Plate Recognition on Kaggle](https://www.kaggle.com/datasets/sahajap99/characters-dataset-for-license-plate-recognition)

### Usage

The code is located in the `LPR/` directory as a Jupyter Notebook (`LPR.ipynb`). It is designed to be run in a Google Colab environment.

**Note:** The notebook has a dependency on Google Drive for loading the dataset and saving models. You will need to mount your Google Drive and adjust the file paths accordingly.

## OldLPR (2018)

This is an older implementation of a license plate recognition system built with traditional computer vision techniques.

### Technology Stack

*   **Python 2**
*   **OpenCV:** Used for image processing and computer vision tasks.
*   **Numpy:** For numerical operations.

### Methodology

The system follows these steps:

1.  **Plate Detection:** The system detects license plates by finding contours in the image that could be characters. It then groups these characters to identify potential license plates.
2.  **Character Recognition:** A K-Nearest Neighbors (KNN) classifier is used to recognize the characters on the detected license plate. The KNN model is trained on pre-classified character images.

### Usage

The main script is `OldLPR(2018)/Main (1).py`. To run the script, you will need the following files in the same directory:

*   `classifications.txt`: Contains the classifications for the training data.
*   `flattened_images.txt`: Contains the flattened image data for training the KNN model.

The script is written in Python 2.

## Future Work

A potential improvement would be to build a single, end-to-end model that combines both license plate detection and character recognition. This could be achieved by using two object detection models:

1.  The first model would detect and crop the license plate from the image.
2.  The second model would detect and classify the characters from the cropped plate image.

## License

This project is licensed under the terms of the license agreement. See the [LICENSE](LICENSE) file for more details.
