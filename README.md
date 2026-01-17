# Deep Learning & 6th Semester Coursework (IILM26)

This repository contains coursework and projects for the 6th semester at IILM, specializing in Deep Learning applications.

## Project Structure

The repository is organized into the following main directories:

### 1. yolov8-trial

This directory contains experiments and implementations related to the YOLOv8 object detection model.

- **Purpose**: Training and testing YOLOv8 on specific datasets.
- **Dataset**: The model is trained on an accident detection dataset.
  - **Download**: You can download the required dataset using the `kaggle_dataset.py` script provided in this directory.
- **Key Files**:
  - `kaggle_dataset.py`: Script to fetch the training data.
  - Model training and inference scripts (e.g., `detection.py`, `accuracy.py`).

### 2. VITH-SEM

This directory houses classworks and assignments for the 6th semester.

- **Content**: Various lab exercises, assignments, and minor projects related to the semester curriculum.

## Setup and Usage

To use the YOLOv8 trial scripts:

1. Navigate to the `yolov8-trial` directory.
2. Install necessary dependencies (ensure you have a Python environment set up).
3. Run `python kaggle_dataset.py` to download the dataset.
4. Use the training or detection scripts as needed.

## Notes

- Ensure you have the content of the `dataset` folder before running training scripts. The folder is excluded from version control to save space.
