# AI Object Detection using YOLOv5, OpenCV, and Python

This project demonstrates my journey in building an AI-powered object detection system using Python 3, the OpenCV library, and the YOLOv5 model. The goal is to detect and classify objects in real-time using a live camera feed.

## Features
- **Real-time Object Detection**: Utilizes a live camera feed to detect and classify objects.
- **YOLOv5 Integration**: Leverages the YOLOv5 model for fast and accurate object detection.
- **Customizable Model**: Supports fine-tuning and loading custom-trained YOLOv5 models.
- **OpenCV for Video Processing**: Uses OpenCV for capturing video and displaying annotated frames.

## Technologies Used
- **Python 3**: The programming language used for this project.
- **YOLOv5**: A state-of-the-art object detection model.
- **OpenCV**: A powerful library for computer vision tasks.

## How It Works
1. The YOLOv5 model is loaded using PyTorch.
2. A live video feed is captured using OpenCV.
3. Each frame from the video feed is passed through the YOLOv5 model for object detection.
4. Detected objects are highlighted with bounding boxes and labeled with their class names and confidence scores.
5. The processed video feed is displayed in a window.
6. Press `q` to exit the application.

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8 or later
- pip (Python package installer)
- A webcam or other video input device

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the YOLOv5 model weights:
   - Place the `yolov5s.pt` file in the project directory.

### Running the Project
To run the object detection script:
```bash
python app.py
```

## File Structure
- `app.py`: Main script for running object detection.
- `requirements.txt`: Contains the list of required Python libraries.
- `yolov5s.pt`: Pre-trained YOLOv5 model weights (not included in the repository).

## Sample Output
The program will display a video feed with objects highlighted by bounding boxes and labeled with their class names and confidence scores. Example objects include people, cars, and various common items.

## Future Improvements
- Add support for custom datasets and training.
- Optimize performance for deployment on edge devices like Raspberry Pi.
- Integrate with other libraries for additional functionality (e.g., saving detected frames).

## Acknowledgments
- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5)
- [OpenCV](https://opencv.org/)

---

Feel free to contribute or reach out with any questions or suggestions!
