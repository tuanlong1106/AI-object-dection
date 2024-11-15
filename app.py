import cv2
import torch

# Tải mô hình YOLOv5 từ tệp local
model = torch.hub.load('.', 'custom', path='yolov5s.pt', source='local')

# Khởi tạo camera với AVFOUNDATION (dành riêng cho macOS)
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Error: Cannot access the camera")
    exit()

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame from camera")
        break

    # Phát hiện đối tượng
    results = model(frame)

    # Vẽ hộp giới hạn và nhãn
    for *box, conf, cls in results.xyxy[0]:
        label = f"{model.names[int(cls)]}: {conf:.2f}"
        cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(box[0]), int(box[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Hiển thị khung hình
    cv2.imshow("MacBook Camera - Object Detection", frame)

    # Thoát bằng phím 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Exiting...")
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()