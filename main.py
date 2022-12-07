#pip install opencv-python
#python3 -m pip install opencv-python
import cv2

def camera():
    # open camera
    cap = cv2.VideoCapture(0)

    for i in range(1):
        cap.read()

    ret, frame = cap.read()

    # write to the file
    cv2.imwrite('cam.png', frame)

    # Close connection camera
    cap.release()

print('start')

# Function
camera()