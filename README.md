# AI Object Detection using YOLOv5 and OpenCV

This project demonstrates real-time object detection using Python 3, the OpenCV library, and the YOLOv5 model. The application is specifically designed to work with the built-in webcam of a MacBook.

## Features
- Real-time object detection with bounding boxes and labels.
- Utilizes YOLOv5 for accurate and fast object detection.
- OpenCV for video capture and display, optimized for macOS.

## Prerequisites
- macOS with a built-in MacBook webcam
- Python 3.8 or later
- pip (Python package manager)

## Setup Instructions

### Step 1: Create a Virtual Environment
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

### Step 2: Clone This Repository
Clone your repository containing `app.py`:
```bash
git clone https://github.com/tuanlong1106/AI-object-dection.git
```

### Step 3: Download YOLOv5 Weights
Download the pre-trained YOLOv5 model weights (`yolov5s.pt`):
```bash
curl -O https://github.com/ultralytics/yolov5/releases/download/v6.0/yolov5s.pt
```

### Step 4: Clone the YOLOv5 Repository
Clone the YOLOv5 repository:
```bash
git clone https://github.com/ultralytics/yolov5.git
```

### Step 5: Move Required Files
Move `app.py` and `yolov5s.pt` into the `yolov5` folder:
```bash
mv AI-object-dection/app.py yolov5/
mv yolov5s.pt yolov5/
```
Ensure the `yolov5` folder contains:
```
yolov5/
├── app.py
├── yolov5s.pt
├── models/
├── data/
└── ...
```

### Step 6: Install Dependencies
Navigate to the `yolov5` folder and install dependencies:
```bash
cd yolov5
pip install -r requirements.txt
```
Install additional dependencies for OpenCV:
```bash
pip install opencv-python
```

### Step 7: Run the Application
Run the `app.py` script to start the object detection application:
```bash
python app.py
```

### Step 8: Interact with the Application
- The application will open a video feed from your MacBook's built-in webcam.
- Detected objects will be highlighted with bounding boxes and labeled with their class names.
- Press `q` to exit the application.

## Troubleshooting
- **Camera Not Working**: Ensure the correct camera index is set in `cv2.VideoCapture`. For example:
  ```python
  cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
  ```
- **Dependencies Not Found**: Double-check the installation of dependencies by running:
  ```bash
  pip install -r requirements.txt
  pip install opencv-python
  ```

## File Structure
- `app.py`: Main script for running object detection.
- `yolov5s.pt`: Pre-trained YOLOv5 model weights.
- `requirements.txt`: List of required Python libraries.
- `README.md`: Documentation for setup and usage.
- `models/`, `data/`: YOLOv5 internal directories.

## Future Improvements
- Support for custom-trained YOLOv5 models.
- Optimize for deployment on edge devices.
- Enhance cross-platform compatibility.

---

Feel free to reach out for support or to contribute to this project!
