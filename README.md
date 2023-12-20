<center><h1 align="center">MLZoomcamp 2023 Capstone Project.</h1></center>

## Project Overview:
This project aims to develop a deep learning model for the classification of corn (maize) plant leaf diseases. The dataset consists of images categorized into four classes: Common Rust, Gray Leaf Spot, Blight, and Healthy. The goal is to train a robust classification model that can accurately identify the specific disease affecting a corn plant based on images of its leaves.

## Dataset:
<a href="https://www.kaggle.com/datasets/smaranjitghose/corn-or-maize-leaf-disease-dataset"> Dataset link </a> 
The dataset comprises a total of 4188 images, distributed across the following classes:

* Common Rust: 1306 images
* Gray Leaf Spot: 574 images
* Blight: 1146 images
* Healthy: 1162 images

The images have been pre-labeled with their respective disease classes to facilitate supervised learning.

## Problem Statement:
Corn is a staple crop worldwide and is susceptible to various diseases that can significantly impact yield and quality. Early detection and accurate classification of plant diseases are crucial for implementing timely interventions such as targeted treatment or removal of infected plants. Traditional methods of disease diagnosis can be time-consuming and may not scale well to large agricultural settings.

Deep learning models offer a promising solution for automating the classification process. By training a neural network on a diverse dataset of corn leaf images, the model can learn to recognize patterns and features indicative of different diseases. The ultimate goal is to deploy the trained model as part of an intelligent system that can assist farmers and agricultural experts in identifying and managing plant diseases effectively.

## Approach:
The project follows a deep learning approach to address the classification task. Convolutional Neural Networks (CNNs), known for their effectiveness in image classification tasks.

Key steps in the approach include:

## Data Preprocessing:

Loading and organizing the dataset.
Augmenting the data to increase model robustness.
Model Training:

Building and training a deep learning model.
Experimenting with different architectures and hyperparameters.
Model Evaluation:

Assessing the model's performance on a separate test set.
Analyzing metrics such as accuracy, precision, recall, and F1 score.
Deployment (Future Consideration):

Preparing the model for deployment in real-world scenarios.
Exploring options for integration into agricultural systems.






<center><h2 align="center">3. How the solution will be used</h2></center>
Given url of user's image, application returns dictionary with class probabilities. Online shop bot chooses the most confident predictions to suggest for user the name of the tomato cultivar needed. User makes an order to purchase seeds of this tomato cultivar.

<center><h2 align="center">4. Description of the repository</h2></center>

1) `notebook.ipynb` - notebook that covers:

  * Data loading, preparation and exploration,
  * Building dataloaders,
  * Building transfer-learning model for image classification with keras,
  * Setting parameters for model,
  * Model training,
  * Monitoring results of the model,
  * Converting tensorflow model to TFLite format.

2) `train.py` - python script to train the model, convert to tflite format and save it.

3) `test.py` - python script to test application.

4) `lambda-function.py` -  python script with function to run application from within the AWS Labmda console.

5) `Dockerfile` - specifies the commands that builds docker image with application.

6) `model.tflite` - tf.keras model converted into TFLite format.

7) `tomatoes.zip` - archived dataset.

8) `readme.md`.

<center><h2 align="center">5. How to run the project</h2></center>

This project supposed to be deployed on AWS Lambda, but this did not happen :(

The validity of the project can be checked in the following way:
* copy (clone) this repository to your local PC to some directory,
* change path to that directory with command line:
```
cd <your-directory-name>
```
* build the docker image:
```
docker build -t tomato-model .
```
* run the docker image with command:
```
docker run -it --rm -p 8080:8080 tomato-model:latest
```
* run the `test.py` script with the image url you want. 
*(check the local IP and paste it instead 'localhost' if you are on Windows)*
* unzip dataset to subfolder `/tomatoes`, if you want to run `train.py` script, or use `!unzip tomatoes.zip` command in the Jupyter notebook
