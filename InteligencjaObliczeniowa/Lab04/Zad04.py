import os
import cv2
import json
from collections import Counter
from ultralytics import YOLO


def detect_yolo(input_path, output_path=None, model_name="yolov8n.pt"):
    model = YOLO(model_name)
    ext = os.path.splitext(input_path)[1].lower()

    if ext in [".jpg", ".jpeg", ".png", ".bmp"]:
        # IMAGE
        output_path = output_path or "output_image.jpg"
        json_path = os.path.splitext(output_path)[0] + ".json"
        results = model(input_path)
        detections_json = []

        img = cv2.imread(input_path)

        for result in results:
            for box in result.boxes:
                data = {
                    "class": int(box.cls[0]),
                    "confidence": float(box.conf[0]),
                    "bbox": [float(x) for x in box.xyxy[0]]
                }
                detections_json.append(data)
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, f'{int(box.cls[0])}:{box.conf[0]:.2f}', (x1, y1 - 5),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imwrite(output_path, img)
        with open(json_path, "w") as f:
            json.dump(detections_json, f, indent=4)

        stats = dict(Counter([d["class"] for d in detections_json]))
        print(f"Image statistics: {stats}")
        return stats

    elif ext in [".mp4", ".avi", ".mov", ".mkv"]:
        # VIDEO
        output_path = output_path or "output_video.mp4"
        json_path = os.path.splitext(output_path)[0] + ".json"

        cap = cv2.VideoCapture(input_path)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        all_detections = []
        frame_idx = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)
            frame_detections = []

            for result in results:
                for box in result.boxes:
                    data = {
                        "frame": frame_idx,
                        "class": int(box.cls[0]),
                        "confidence": float(box.conf[0]),
                        "bbox": [float(x) for x in box.xyxy[0]]
                    }
                    frame_detections.append(data)
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f'{int(box.cls[0])}:{box.conf[0]:.2f}', (x1, y1 - 5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

            all_detections.extend(frame_detections)
            out.write(frame)
            frame_idx += 1

        cap.release()
        out.release()
        with open(json_path, "w") as f:
            json.dump(all_detections, f, indent=4)

        stats = dict(Counter([d["class"] for d in all_detections]))
        print(f"Video statistics: {stats}")
        return stats

    else:
        raise ValueError("Unsupported file type. Use image or video.")

detect_yolo("street_yolo.mp4")
