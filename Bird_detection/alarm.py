import cv2
import winsound  # For Windows sound alarm

# Load the Haar cascades for detecting drones
drone_cascade = cv2.CascadeClassifier('drone-cascade.xml')

# Open the webcam
cap = cv2.VideoCapture(0)

# Define the alarm sound
def play_alarm():
    winsound.Beep(1000, 1000)  # Frequency (Hz), Duration (ms)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect drones
    drones = drone_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(drones) > 0:
        # Draw rectangle around the detected drones
        for (x, y, w, h) in drones:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'Drone', (x - 10, y - 10), font, 0.5, (0, 255, 255), 2, cv2.LINE_AA)
        
        # Play alarm sound
        play_alarm()
    else:
        # Display error message
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Error: No Drone Detected!', (10, 30), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
    
    # Show the frame
    cv2.imshow('img', img)
    
    # Exit on 'Esc' key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
