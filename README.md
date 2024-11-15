# AI Object Detection using YOLOv5 and OpenCV

This project demonstrates real-time object detection using Python 3, the OpenCV library, and the YOLOv5 model.

## Features
- Real-time object detection with bounding boxes and labels.
- Utilizes YOLOv5 for accurate and fast object detection.
- OpenCV for video capture and display.

## Prerequisites
- Python 3.8 or later
- pip (Python package manager)
- A webcam or other video input device

## Setup Instructions

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/tuanlong1106/AI-object-dection.git
cd AI-object-dection
```

### Step 2: Clone YOLOv5 Repository
Download the YOLOv5 repository, which includes the pre-trained model and code:
```bash
git clone https://github.com/ultralytics/yolov5.git
```

Ensure the YOLOv5 folder is in the same directory as `app.py` and `yolov5s.pt`:
```
AI-object-dection/
├── app.py
├── yolov5/
└── yolov5s.pt
```
This ensures that `app.py` and `yolov5s.pt` are correctly aligned with the YOLOv5 code.

### Step 3: Set Up a Virtual Environment
Create and activate a virtual environment to isolate dependencies:
- **On macOS/Linux**:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```
- **On Windows**:
  ```bash
  python -m venv env
  .\env\Scripts\activate
  ```

### Step 4: Install Dependencies
Install the required libraries listed in the YOLOv5 repository:
```bash
pip install -r yolov5/requirements.txt
```

Install additional libraries for OpenCV and any other dependencies:
```bash
pip install opencv-python
```

### Step 5: Download YOLOv5 Weights
Download the pre-trained YOLOv5 model weights (`yolov5s.pt`) from the [YOLOv5 GitHub repository](https://github.com/ultralytics/yolov5/releases) and place it in the `AI-object-dection` directory, ensuring it is accessible by `app.py`.

### Step 6: Update `app.py` Path
In `app.py`, ensure the YOLOv5 model is loaded correctly by specifying the relative or absolute path to the YOLOv5 folder and weights:
```python
model = torch.hub.load('yolov5', 'custom', path='yolov5s.pt', source='local')
```

### Step 7: Run the Application
Execute the `app.py` script to start the object detection application:
```bash
python app.py
```

### Step 8: Interact with the Application
- The application will open a video feed from your webcam.
- Detected objects will be highlighted with bounding boxes and labeled with their class names.
- Press `q` to exit the application.

## Troubleshooting
- **Camera Not Working**: Ensure the correct camera index is set in `cv2.VideoCapture`. For example:
  ```python
  cap = cv2.VideoCapture(0)
  ```
- **Dependencies Not Found**: Double-check the installation of dependencies by running:
  ```bash
  pip install -r yolov5/requirements.txt
  pip install opencv-python
  ```

## File Structure
- `app.py`: Main script for running object detection.
- `requirements.txt`: List of required Python libraries.
- `README.md`: Documentation for setup and usage.
- `yolov5/`: YOLOv5 repository folder containing models and code.

## Future Improvements
- Support for custom-trained YOLOv5 models.
- Optimize for deployment on edge devices.
- Enhance cross-platform compatibility.

---

Feel free to reach out for support or to contribute to this project!
