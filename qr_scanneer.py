
import cv2
from datetime import datetime

# Advanced Detector
detector = cv2.QRCodeDetector()
cap = cv2.VideoCapture(0)
scanned_list = set()

print("Show me QR Code")

while True:
    success, frame = cap.read()
    if not success:
        print("Camera access Denied")
        break

    # QR Code Scaning Try
    # detectAndDecodeMulti Use of that code is make process fast
    data, bbox, _ = detector.detectAndDecode(frame)

    if data: # if data is find
        if data not in scanned_list:
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            
            # File mein save karein
            with open("attendance.csv", "a") as f:
                f.write(f"{data},{dt_string}\n")
            
            print(f"SUCCESS: {data} Scanned sucessfull!")
            scanned_list.add(data)
            
            # Screen par feedback dikhane ke liye
            cv2.putText(frame, "SCAN SUCCESS", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Window display
    cv2.imshow('QR Attendance Scanner', frame)

    # 'x' for close windows
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()