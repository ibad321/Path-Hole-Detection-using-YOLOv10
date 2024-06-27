# Path-Hole-Detection-using-YOLOv10

This project focuses on detecting path holes in real-time from video feeds using the YOLOv10 model. The model is trained on a custom dataset downloaded from Roboflow and can be tested on video files using the provided scripts.

## Table of Contents
- [Dataset](#dataset)
- [Training the Model](#training-the-model)
- [Downloading the Pretrained Model](#downloading-the-pretrained-model)
- [Testing the Model](#testing-the-model)
- [Requirements](#requirements)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

## Dataset
1. **Download the Dataset**: 
   - Go to [Roboflow](https://roboflow.com) and download the path hole detection dataset.
   - Ensure you have the dataset in a suitable format (e.g., COCO format).

## Training the Model
1. **Train YOLOv10 on Google Colab or Kaggle**:
   - Upload the dataset to your Colab or Kaggle environment.
   - Use the provided training script to train the YOLOv10 model.

## Downloading the Pretrained Model
1. **Download the Pretrained Model (best.pt)**:
   - After training, download the `best.pt` file from the weights folder in your Colab or Kaggle environment.

## Testing the Model
1. **Test the Model on Video**:
   - Use the `main.py` script provided in this repository to test the model on your video file.

## Requirements
- Python 3.x
- OpenCV
- Pandas
- cvzone
- ultralytics

## Usage
1. **Install the required packages**:
   ```bash
   pip install opencv-python pandas cvzone ultralytics
2. **Run the main.py script**:
   ```bash
   python main.py
## Acknowledgements

- Roboflow for the dataset.
- Ultralytics for the YOLOv10 model.

## Contact

If you have any questions or suggestions about this project, feel free to reach out to me.

- **Email**: [ibadcui@gmail.com](mailto:ibadcui@gmail.com)
- **LinkedIn**: [Ibad's LinkedIn](https://www.linkedin.com/in/ibad321/)

