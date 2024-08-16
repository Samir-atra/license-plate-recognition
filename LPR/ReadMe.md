# License plate recognition

a project built to be integrated on a camera system, to be able to detect and classify license plates in real-time.

the model built today consists of two parts the first one using ImageAI library which functions as a license plates detector in the image,

the second part of the model is a RNN model that process the image as a time series data and in perfect case will be able to crop the image many times into it's character and the characters later to be classified using a classification algorithm trained on a numbers images dataset.

the datasets used now are:
- For license plate detection: https://www.kaggle.com/datasets/andrewmvd/car-plate-detection

- for character detection and classification: https://www.kaggle.com/datasets/sahajap99/characters-dataset-for-license-plate-recognition

this project is more about improving the older's version metrics and learning then coming with a new approach than to delivering a solution.

## suggested future work

a new approach could be developed for the same application is building a single model that consists of two object detection algorithms the first get trained to detect license plates in images and crop them, the second algorithm is to detect the characters in the cropped plate and classify them, then print them into text.