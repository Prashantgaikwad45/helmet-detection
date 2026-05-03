from ultralytics import YOLO
import cv2

# Load your YOLOv8 Nano model
model = YOLO("yolov8n.pt")  # this is your model file

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)   # height

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame)

    # Draw detection boxes
    annotated_frame = results[0].plot()

    # Simple logic: if person detected → ALERT (simulate helmet detection)
    helmet_detected = True  # assume safe

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            # print(label)  # uncomment to see what YOLO detects
            if label == "person":
                helmet_detected = False  # assume no helmet for demo

    # Display alert text
    if not helmet_detected:
        cv2.putText(annotated_frame, "ALERT: No Helmet!", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
    else:
        cv2.putText(annotated_frame, "SAFE: Helmet Detected", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

    # Show frame
    cv2.imshow("Helmet Detection Demo", annotated_frame)

    # Exit with ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()