import cv2
import os
from detector import ObjectDetector
from utils import FPSCounter, draw_detections, draw_hud
from deep_sort_realtime.deepsort_tracker import DeepSort

# GLOBAL LOCK VARIABLE
locked_id = None

def estimate_distance(box_width):
    focal_length = 700
    real_width = 0.5
    distance = (real_width * focal_length) / box_width
    return round(distance, 2)

def main():
    global locked_id

    print("[INFO] Starting DRDO-Level Drone System...")

    detector = ObjectDetector()
    tracker = DeepSort(max_age=30)
    fps_counter = FPSCounter()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Camera not accessible")
        return

    os.makedirs("output", exist_ok=True)

    out = cv2.VideoWriter(
        "output/output.mp4",
        cv2.VideoWriter_fourcc(*'mp4v'),
        20,
        (640, 480)
    )

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))

        # DETECTION
        detections = detector.detect(frame)

        # TRACKING INPUT
        tracker_inputs = []
        for det in detections:
            x1, y1, x2, y2 = det["box"]
            w = x2 - x1
            h = y2 - y1
            tracker_inputs.append(([x1, y1, w, h], det["confidence"], det["label"]))

        tracks = tracker.update_tracks(tracker_inputs, frame=frame)

        # DRAW DETECTIONS
        accuracy = draw_detections(frame, detections)

        # DRAW TRACKS
        for track in tracks:
            if not track.is_confirmed():
                continue

            track_id = track.track_id
            l, t, r, b = map(int, track.to_ltrb())

            color = (255, 0, 0)

            # LOCKED TARGET
            if track_id == locked_id:
                color = (0, 0, 255)
                cv2.putText(frame, "LOCKED TARGET",
                            (l, t - 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            color,
                            2)

            cv2.rectangle(frame, (l, t), (r, b), color, 2)
            cv2.putText(frame, f"ID {track_id}",
                        (l, t - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color,
                        2)

        # DISTANCE ESTIMATION
        for det in detections:
            x1, y1, x2, y2 = det["box"]
            width = x2 - x1

            if width > 0:
                dist = estimate_distance(width)

                cv2.putText(frame, f"{dist}m",
                            (x1, y2 + 20),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5,
                            (255, 255, 0),
                            2)

        # THREAT CLASSIFICATION
        threat = "LOW"
        for det in detections:
            if det["label"] == "person" and det["confidence"] > 0.7:
                threat = "HIGH"
            elif det["label"] in ["car", "truck"]:
                threat = "MEDIUM"

        color = (0, 255, 0)
        if threat == "HIGH":
            color = (0, 0, 255)
        elif threat == "MEDIUM":
            color = (0, 255, 255)

        cv2.putText(frame, f"THREAT: {threat}",
                    (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2)

        # FPS + HUD
        fps = fps_counter.get_fps()
        draw_hud(frame, fps, accuracy)

        # SHOW
        cv2.imshow("DRDO Drone System", frame)

        # SAVE
        out.write(frame)

        # CONTROLS
        key = cv2.waitKey(1) & 0xFF

        # LOCK TARGET
        if key == ord('l'):
            for track in tracks:
                if track.is_confirmed():
                    locked_id = track.track_id
                    print(f"[INFO] Locked Target ID: {locked_id}")
                    break

        # DRONE CONTROL SIMULATION
        if key == ord('w'):
            print("Drone Moving Forward")
        if key == ord('s'):
            print("Drone Moving Backward")
        if key == ord('a'):
            print("Drone Moving Left")
        if key == ord('d'):
            print("Drone Moving Right")

        # EXIT
        if key == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()