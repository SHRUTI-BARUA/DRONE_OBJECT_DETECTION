from ultralytics import YOLO

class ObjectDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        results = self.model(frame, verbose=False)

        detections = []

        for r in results:
            for box in r.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = self.model.names[cls]

                detections.append({
                    "box": [x1, y1, x2, y2],
                    "confidence": conf,
                    "label": label
                })

        return detections