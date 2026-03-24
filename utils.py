import time
import cv2

class FPSCounter:
    def __init__(self):
        self.prev_time = time.time()

    def get_fps(self):
        curr_time = time.time()
        fps = 1 / (curr_time - self.prev_time)
        self.prev_time = curr_time
        return int(fps)

def draw_detections(frame, detections):
    total_conf = 0

    for det in detections:
        x1, y1, x2, y2 = det["box"]
        conf = det["confidence"]
        label = det["label"]

        total_conf += conf

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f"{label} {conf:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0,255,0),
                    2)

    if len(detections) == 0:
        return 0

    return total_conf / len(detections)

def draw_hud(frame, fps, accuracy):
    cv2.putText(frame, f"FPS: {fps}",
                (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2)

    cv2.putText(frame, f"Accuracy: {accuracy:.2f}",
                (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2)