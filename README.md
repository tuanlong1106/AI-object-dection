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

### Step 1: Clone the YOLOv5 Repository
Download the YOLOv5 repository, which includes the pre-trained model and code:
```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
```

### Step 2: Place Required Files
Ensure the following files are placed in the `yolov5` folder:
- `app.py`: The main script for object detection.
- `yolov5s.pt`: The pre-trained YOLOv5 weights file.

The folder structure should look like this:
```
yolov5/
├── app.py
├── yolov5s.pt
├── models/
├── data/
└── ...
```

### Step 3: Set Up a Virtual Environment
Create and activate a virtual environment to isolate dependencies:
- **On macOS**:
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

### Step 4: Install Dependencies
Install the required libraries listed in the YOLOv5 repository:
```bash
pip install -r requirements.txt
```

Install additional libraries for OpenCV and any other dependencies:
```bash
pip install opencv-python
```

### Step 5: Update `app.py` Path
In `app.py`, ensure the YOLOv5 model is loaded correctly by specifying the relative path within the `yolov5` folder:
```python
model = torch.hub.load('.', 'custom', path='yolov5s.pt', source='local')
```

### Step 6: Run the Application
Navigate to the `yolov5` directory and execute the `app.py` script to start the object detection application:
```bash
python app.py
```

### Step 7: Interact with the Application
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
