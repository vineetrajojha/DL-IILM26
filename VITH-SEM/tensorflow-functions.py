# ==========================================================
# TensorFlow Object Detection – Top 10 Core Functions
# ==========================================================
# This file documents the most important TensorFlow functions
# used in modern object detection systems like YOLO, SSD,
# Faster-RCNN, and the TensorFlow Object Detection API.
#
# Object Detection Output:
# - Bounding boxes
# - Class labels
# - Confidence scores
#
# Core Pipeline:
# Input Image -> Resize -> CNN Feature Extraction -> Prediction
# -> Post Processing (NMS) -> Final Detections
# ==========================================================


# 1. tf.image.non_max_suppression()
# Removes duplicate and overlapping bounding boxes by keeping
# only the highest confidence prediction.
# Used after model prediction to clean detection results.


# 2. tf.image.resize()
# Resizes input images to the required model input size
# such as 300x300 or 640x640 before feeding into the network.


# 3. tf.keras.applications (ResNet, MobileNet, EfficientNet)
# Pre-trained CNN backbone networks that extract visual features
# like edges, shapes, and textures from images.
# Examples:
# - ResNet50
# - MobileNetV2
# - EfficientNetB0


# 4. tf.keras.layers.Conv2D()
# Core building block of convolutional neural networks.
# Detects patterns such as edges, shapes, objects, and textures.


# 5. tf.image.crop_and_resize()
# Crops detected object regions from the original image.
# Used in models like Faster-RCNN and Mask-RCNN for region refinement.


# 6. tf.keras.losses.Huber()
# Calculates bounding box regression loss.
# Helps the model learn how accurate its predicted box positions are.


# 7. tf.keras.losses.SparseCategoricalCrossentropy()
# Calculates classification loss.
# Teaches the model what object class is present in each bounding box.


# 8. tf.data.Dataset.from_tensor_slices()
# Creates an efficient data pipeline for training.
# Loads images and labels into TensorFlow in batches.


# 9. tf.keras.Model.predict()
# Runs inference on input images.
# Outputs bounding boxes, class labels, and confidence scores.


# 10. tf.saved_model.load()
# Loads a trained TensorFlow object detection model.
# Used during deployment or real-time inference.


# ==========================================================
# Summary
# ==========================================================
# These functions together enable:
# - Image preprocessing
# - Feature extraction
# - Model training
# - Object detection
# - Post-processing of predictions
#
# They form the foundation of real-world AI systems such as
# security cameras, autonomous vehicles, and surveillance.
# ==========================================================
