import cv2
from ocr_module import detect_plate
from db_module import insert_plate
import imutils

cap = cv2.VideoCapture(0)  # 0 for default camera

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = imutils.resize(frame, width=800)

    plate_text, frame = detect_plate(frame)

    if plate_text:
        print(f"Detected Number Plate: {plate_text}")
        inserted_id = insert_plate(plate_text)
        print(f"Inserted into DB with ID: {inserted_id}")

    cv2.imshow("Number Plate Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
